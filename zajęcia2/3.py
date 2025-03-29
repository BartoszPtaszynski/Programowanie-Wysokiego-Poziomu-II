from typing import Dict, Optional

class Library:
    def __init__(self):
        self.books: Dict[str, str] = {}

    def add_book(self, isbn: str, title: str) -> None:
        self.books[isbn] = title

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)

library = Library()
library.add_book("978-3-16-148410-0", "Python dla każdego")
print(library.find_book("978-3-16-148410-0"))
print(library.find_book("123-4-56-789012-3"))