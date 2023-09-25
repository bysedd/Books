import logging
from datetime import datetime

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, show_path=False)]
)


def func_log(func):
    """
    :param func: A function object that needs to be logged.
    :return: A decorated function that logs the execution time of the provided function.
    """

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        time_lapse = round((end - start).total_seconds(), 1)
        logging.info(f"Executed '{func.__name__}' in {time_lapse}s")
        return result

    return wrapper


def log(message):
    """
    Log a message.
    """
    logging.info(message)


if __name__ == '__main__':
    @func_log
    def example_func():
        # Simulating a function that takes a bit of time to execute
        import time
        from random import randint
        time.sleep(randint(1, 3))

    example_func()
