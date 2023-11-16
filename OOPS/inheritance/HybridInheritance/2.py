class Book:
    def __init__(self, title):
        self.title = title


class Author(Book):
    def __init__(self, title, auth_name):
        Book.__init__(self, title)
        self.auth_name = auth_name


class Genre(Book):
    def __init__(self, title, genre):
        Book.__init__(self, title)
        self.genre = genre


class Reader(Author, Genre):
    def __init__(self, title, auth_name, genre, red_name):
        Author.__init__(self, title, auth_name)
        Genre.__init__(self, title, genre)
        self.red_name = red_name

    def read_book(self):
        print(f"{self.red_name} is reading {self.title} by {self.auth_name} of genre {self.genre}.")


obj = Reader("The Lord of the Rings",
             "J.R.R. Tolkien",
             "Fantasy",
             "Alice")

obj.read_book()
