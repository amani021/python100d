#-------- DAY 46 & 47 "exercise" --------
class library:
    def __init__(self, shelf, book):
        self.shelf = shelf
        self.book = book

class science_section(library):
    def __init__(self, shelf, book, name):
        super().__init__(shelf, book)
        self.name = name
        self.shelf = 4
        self.book = 20

# obj1 = library(45, 300)
obj2 = science_section(45, 300, 'Physiscs books')
print('The library have', obj2.shelf, 'shelves which contain', obj2.book, obj2.name)
