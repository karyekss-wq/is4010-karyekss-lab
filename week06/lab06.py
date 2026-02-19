class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"\"{self.title}\" by {self.author} ({self.year})"

    def get_age(self) -> int:
        return 2025 - self.year


class EBook(Book):
    def __init__(self, title: str, author: str, year: int, file_size: int) -> None:
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self) -> str:
        return f"{super().__str__()} ({self.file_size} MB)"


if __name__ == "__main__":
    book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    ebook = EBook("Dune", "Frank Herbert", 1965, 5)

    print(book)
    print(f"Book age: {book.get_age()} years")
    print(ebook)
    print(f"EBook age: {ebook.get_age()} years")
