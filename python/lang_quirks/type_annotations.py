from typing import List


def log_start_and_end(func):
    """Log a message before and after executing the wrapped function"""

    def wrapper(*args, **kwargs):
        print(f"Starting function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finishing function: {func.__name__}")
        return result

    return wrapper


@log_start_and_end
def broken_func_def(foo: List[int]):
    for i in foo:
        print(i)


if __name__ == "__main__":
    broken_func_def(6)  # type: ignore
