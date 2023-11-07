class Student:

    def __init__(self, name, age, grade, scores):
        self.name = name
        self.age = age
        self.grade = grade
        self.scores = scores



    def info(self):
        print('Имя:', self.name)
        print(f'Возраст: {self.age}')
        print(f'Класс: {self.grade}')
        print(f'Оценки: {self.scores}')

    def average_score(self):
        return sum(self.scores) / len(self.scores)


student2 = Student("Галиев Даниил", 12, "9Г", [5, 4, 4, 5])
student2.info()
print('Средний балл', student2.average_score())
