import logging
from datetime import datetime

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="[%X]",
    handlers=[
        RichHandler(
            rich_tracebacks=True, show_path=False, show_time=False, show_level=False
        )
    ],
)


def func_log(func):
    """
    :param func: A function object that needs to log.
    :return: A decorated function that logs the executing time of the provided function.
    """

    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        time_lapse = round((end - start).total_seconds(), 1)
        log(f"Executed '{func.__name__}' in {time_lapse}s")
        return result

    return wrapper


def log(message):
    """
    Log a message.
    """
    logging.info(message)


if __name__ == "__main__":

    @func_log
    def example_func():
        # Simulating a function that takes a bit of time to execute
        import time
        from random import randint

        time.sleep(randint(1, 3))

    example_func()
