'''
In a mystical library, books hold secrets. Create a Book class with a
content() method revealing book details. Derive FantasyBook and
SciFiBook classes inheriting Book. Use recursion to display the content
of each book. Instructions: Define a Book class with a content() method
that presents book details. Derive FantasyBook and SciFiBook classes
inheriting Book, overriding content(). Utilize recursion to showcase the
content of both a Fantasy Book and a Sci-Fi Book.
'''
class Book:
    def __init__(self):
        self.name = "Book 1"
        self.price = "123"

    def Content(self):
        print(f"\n Name : {self.name} - Price : {self.price}",end="")


class FantasyBook(Book):
    def __init__(self):
        self.name = "Fantasy1"
        self.price = "500"
        self.type = "Fantasy"
        self.available = "yes"

    def Content(self):
        super().Content()
        print(f"Type : {self.type} - available : {self.available}")

class SciFicBook(Book):
    def __init__(self):
        self.name = "Science Fiction Book"
        self.price = "1000"
        self.type = "Science Fiction"
        self.available = "yes"
        self.author = "xyz"

    def Content(self):
       Fant = FantasyBook()
       Fant.Content()
       super().Content()
       print(f"Type : {self.type} - available : {self.available} - Author : {self.author}")


obj = SciFicBook()
obj.Content()
