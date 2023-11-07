class Book:

    def __init__(self, name, author, isbn):
        self.__name = name
        self.__author = author
        self.__isbn = isbn

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, isbn):
        self.__isbn = isbn


b = Book('name', 'auth1', 1243123412)
print(b.get_author())
b.set_author('auth2')
t = (b.get_author())
print(t*3)
b.set_name('name2')
print(b.get_name())

