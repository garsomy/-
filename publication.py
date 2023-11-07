class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print('Название:', self.title)
        print(f'Автор, {self.author}')
        print(f'Год выхода: {self.year}')

class Book(Publication):

    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')

class Magazine(Publication):

    def __init__(self, title, author, year, issue_num):
        super().__init__(title, author, year)
        self.issue_num = issue_num

    def display(self):
        super().display()
        print(f'Номер журнала: {self.issue_num}')


def info(obj):
    obj.display()

p = Publication('Название1', 'автор1', 2021)
# info(p)
# print()
b = Book('Название2', 'автор2', 2018, 2425462582)
# info(b)
# print()
m = Magazine('Название3', 'автор3', 2012, 14)
# info(m)
list = []
list.append(p)
list.append(b)
list.append(m)
for i in list:
    info(i)
    print()



#Это пример, не нужно записывать(((
# c = 3.1415
# c = int(c)
# c = str(c)
# print(c)
#
# print(2 + 2)
# print('2' + '2')
