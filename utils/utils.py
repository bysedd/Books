import re


def validate_string(
    value: str, field_name: str, min_length: int = 3, max_length: int = 200
) -> None:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string")
    if not value:
        raise ValueError(f"{field_name} cannot be empty")
    if not bool(re.fullmatch("[A-Za-z ]+", value)):
        raise ValueError(f"{field_name} must contain only alphabets and spaces")
    if min_length <= len(value) <= max_length:
        raise ValueError(f"{field_name} cannot exceed {max_length} characters")


def validate_name(name: str, min_length: int = 3) -> None:
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    if len(name) < min_length:
        raise ValueError(f"Name must be at least {min_length} characters long")
    if not bool(re.fullmatch("[A-Za-z ]+", name)):
        raise ValueError("Name must contain only alphabets and spaces")


def alt_title(string: str) -> str:
    """
    Capitalize the first letter of each word in a string if length is greater than 2.
    """
    return " ".join(
        word.capitalize() if len(word) > 2 else word for word in string.split()
    )


def title_msg(string: str) -> str:
    """
    Capitalize the first letter of each word in a string.
    """
    string = f"{'-' * 20} {string} {'-' * 20}"
    return string.title()


def get_option(options: list[str]) -> str:
    """
    Get an option from a list of options.
    """
    print("Available options:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    while True:
        try:
            choice = int(input("Enter choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            raise ValueError
        except ValueError:
            print("Invalid choice. Try again.")
