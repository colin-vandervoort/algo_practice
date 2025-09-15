import docker
import pytest
from sqlalchemy import create_engine, text

from python.tools.sql_solution_testing.sql_solution_testing.managed_container import (
    DEFAULT_DATABASE_HEALTHY_WAIT_TIME_SECONDS,
    ManagedContainer,
    tcp_poll,
)

# from sqlalchemy.engine import Row
# from sqlalchemy.orm import Session


def test_alpine_hello_world():
    echoed_str = "hello world"
    container_id = None
    with ManagedContainer("alpine", f"echo -n {echoed_str}") as container:
        container_id = container.id
        assert container.logs() == bytes(echoed_str, encoding="utf-8")

    if container_id is not None:
        client = docker.from_env()
        try:
            container = client.containers.get(container_id=container_id)
            container.remove()
            pytest.fail("Container was not removed after manager went out of scope.")
        except Exception as e:
            # client.containers.get can throw docker.errors.NotFound or docker.errors.APIError
            # in this case, docker.errors.NotFound being thrown indicates successful cleanup by the handler
            # unfortunately, these classes are not exposed in the public API, so the base Exception class has to be used for matching instead
            if type(e).__name__ == "docker.errors.APIError":
                pytest.fail("Could not connect to daemon")
    else:
        pytest.fail("Container id was never set, cannot check for cleanup.")


def test_mysql_ddl_dml_dql():
    container_id = None
    mysql_root_pass = "example_root_pass"
    mysql_user = "example_user"
    mysql_pass = "example_pass"
    mysql_database = "sql_solution_testing"
    env = {
        "MYSQL_ROOT_PASSWORD": mysql_root_pass,
        "MYSQL_USER": mysql_user,
        "MYSQL_PASSWORD": mysql_pass,
        "MYSQL_DATABASE": mysql_database,
    }
    host_port = 6606
    ports = {
        "3306/tcp": host_port,
    }
    connection_string = f"mysql+pymysql://{mysql_user}:{mysql_pass}@localhost:{host_port}/{mysql_database}?charset=utf8mb4"
    with ManagedContainer(
        "mysql",
        command=None,
        health_check=lambda: tcp_poll(
            "localhost", host_port, DEFAULT_DATABASE_HEALTHY_WAIT_TIME_SECONDS
        ),
        environment=env,
        ports=ports,
    ) as container:
        container_id = container.id
        engine = create_engine(connection_string)
        with engine.connect() as connection:
            max_allowed_packet_result = connection.execute(
                text("SHOW VARIABLES LIKE 'max_allowed_packet'")
            )
            max_allowed_packet_result_row = max_allowed_packet_result.fetchone()
            if max_allowed_packet_result_row is not None:
                print(max_allowed_packet_result_row)
            else:
                pytest.fail("Couldn't retrieve max_allowed_packet")

            connection.execute(
                text(
                    "CREATE TABLE users (id INTEGER PRIMARY KEY AUTO INCREMENT, name TEXT)"
                )
            )
            connection.execute(
                text("INSERT INTO users (name) VALUES (:name)"), {"name": "Alice"}
            )
            result = connection.execute(
                text("SELECT * FROM users WHERE name = :name"), {"name": "Alice"}
            )
            row = result.fetchone()
            if row is not None:
                print(row)
            else:
                pytest.fail("No results returned by query")

    if container_id is not None:
        client = docker.from_env()
        try:
            container = client.containers.get(container_id=container_id)
            container.remove()
            pytest.fail("Container was not removed after manager went out of scope.")
        except Exception as e:
            # client.containers.get can throw docker.errors.NotFound or docker.errors.APIError
            # in this case, docker.errors.NotFound being thrown indicates successful cleanup by the handler
            # unfortunately, these classes are not exposed in the public API, so the base Exception class has to be used for matching instead
            if type(e).__name__ == "docker.errors.APIError":
                pytest.fail("Could not connect to daemon")
    else:
        pytest.fail("Container id was never set, cannot check for cleanup.")
