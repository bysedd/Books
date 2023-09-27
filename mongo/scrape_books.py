from typing import List, Dict

import requests
from bs4 import BeautifulSoup

from utils.constants import BASE_DIR
from utils.formatters import format_title, format_price
from utils.logger import func_log

if __name__ == '__main__':
    @func_log
    def scrape_books() -> List[Dict[str, str | float]]:
        """
        Scrape books information from the 'https://books.toscrape.com' website.

        :return: A list of dictionaries containing the scraped book information.
                 Each dictionary has the keys 'title' and 'price' in a pound.
        """
        books_ = []
        for page in range(1, 51):
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            books_list = soup.find_all("article", attrs={"class": "product_pod"})
            for book_ in books_list:
                title = book_.find("h3").find("a")["title"]
                price = book_.find("p", attrs={"class": "price_color"}).text
                books_.append({"title": format_title(title), "price": format_price(price)})
        return books_

    def write_books(books_: List[Dict[str, float]]) -> None:
        """
        This method takes a list of books and writes the titles of the books to a text file named “books.txt” located
        in the “data” subdirectory of the base directory. The titles appear on separate lines in the file. If a
        book's length exceeds 10 characters, so write to the file.

        :param books_: A list containing dictionaries representing books. Each dictionary should have a “title” key
         to correspond to the title of each book.
        """
        with open(BASE_DIR / "data" / "books.txt", "w", encoding="utf-8") as file:
            for book in books_:
                title = str(book["title"])
                if 10 <= len(title) <= 24:
                    file.write(f"{title}\n")

    books = scrape_books()
    write_books(books)
