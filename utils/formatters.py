import re


def format_title(title):
    """
    Format the title of the book.
    """
    # Remove matched patterns and strip-trailing spaces
    title = re.sub(r"[\[(].*?[)\]]|(?<=:).*$|(?<=-).*$|(?<=;).*$|(?<=,).*$", "", title).strip()

    # Remove special characters
    title = re.sub(r"[^a-zA-Z0-9\s]", "", title)

    # Remove the spaces for each word
    title = " ".join([word.strip() for word in title.split()])

    # Remove the quotation marks
    title = title.replace('"', '')
    title = title.replace("'", '')

    return title


def format_price(price: str):
    """
    Format the price of the book.
    """
    # Remove the unknown and pound character
    price = price[2:]
    # Convert to float
    price = float(price)

    return price
