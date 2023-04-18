class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        pass
    
    def __str__(self):
        return self.title + " by " + self.author

book = Book("A Book", "Me")
print(book)