import re


def format_title(title: str) -> str:
    """
    Format the title of the book.

    :param title: The title of the book.
    :return: The formatted title of the book.
    """
    # Remove matched patterns, special characters, and quotation marks, then strip spaces for each word
    title = re.sub(
        r"[\[(].*?[)\]]|(?<=:).*$|(?<=-).*$|(?<=;).*$|(?<=,).*$|[^a-zA-Z0-9\s]|['\"]",
        "",
        title,
    )
    title = " ".join(title.split())
    return title


def format_price(price: str) -> float:
    """
    Format the price of the book.

    :param price: The price of the book in a pound.
    :return: The price of the book as a float.
    """
    return float(price[2:])
