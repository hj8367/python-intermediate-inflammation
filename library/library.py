class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        pass
    
    def __str__(self):
        return self.title + " by " + self.author


class Library:
    def __init__(self, books=None) -> None:
        if books is None:
            self.books = []
        else:
            self.books = books
        self.titles = []
        self.authors = []
        pass
    
    def __len__(self):
        return len(self.books)

    def add_book(self, name, author):
        assert type(name) == str
        assert type(author) == str

        new_book = Book(name, author)
        self.books.append(new_book)
        self.titles.append(name)
        if author not in self.authors:
            self.authors.append(author)
        pass

    def by_author(self, author):
        assert type(author) == str
        books_by_author = []
        for book in self.books:
            if book.author == author:
                books_by_author.append(book)
        
        if not books_by_author:
            raise KeyError("Author does not exist")

        return books_by_author
    
    def union(self, other):
        books = []
        for book in self.books:
            if book not in books:
                books.append(book)

        for book in other.books:
            if book not in books:
                books.append(book)

        return Library(books)
