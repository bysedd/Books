import logging

from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(message)s",
    datefmt="[%X]",
    handlers=[
        RichHandler(
            rich_tracebacks=True,
            show_path=False,
            show_time=False,
            show_level=False,
        )
    ],
)


def log(message):
    """
    Log a message.
    """
    logging.info(message)
