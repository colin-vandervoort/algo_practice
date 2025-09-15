"""Provides the ManagedContainer class."""

import socket
import time
from typing import Final, List, Protocol

import docker

DEFAULT_DATABASE_HEALTHY_WAIT_TIME_SECONDS: Final = 15


class BlockingHealthCheck(Protocol):
    def __call__(self, *args, **kwargs) -> bool: ...


def tcp_poll(host: str, port: int, duration: int) -> bool:
    for _ in range(duration):
        try:
            with socket.create_connection((host, port), timeout=1):
                return True
        except (ConnectionRefusedError, socket.timeout):
            time.sleep(1)
    return False


class UnhealthyContainerError(Exception):
    pass


def _default_health_check():
    return True


class ManagedContainer:
    def __init__(
        self,
        image_name: str,
        command: str | List[str] | None = None,
        health_check: BlockingHealthCheck = _default_health_check,
        *args,
        **kwargs,
    ):
        r"""Construct a new :class:`ManagedContainer`.

        :param image_name: The name of the container image to run.

        :param command: The command to run inside of the container on startup.

        :param health_check: A blocking function to call to wait until the container is ready
        """
        self.image_name = image_name

        print(f"Running container from image: {self.image_name}")
        client = docker.from_env()
        self.container = client.containers.run(
            self.image_name, command, *args, **kwargs, detach=True
        )

        if (healthy := health_check) is not None:
            if not healthy():
                raise UnhealthyContainerError(f"{self.image_name} failed health check")

    def __enter__(self):
        return self.container

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        return self.close()

    def close(self) -> bool:
        if self.container:
            self.container.stop()
            self.container.remove()

        # return False if method completed successfully
        return False
