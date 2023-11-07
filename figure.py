class Figure:

    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color

    def draw(self):
        print(f'Рисуем фигуру. Цвет: {self.color} и ширина {self.width}')

class Line(Figure):

    def draw(self):
        print(f'Рисуем линию. Цвет: {self.color} и ширина {self.width}')

    def del_line(self):
        print('Линия удалена')

class Rect(Figure):

    def __init__(self, coords, width, color, right):
        super().__init__(coords, width, color)
        self.right = right

    def draw(self):
        print(f'Рисуем прямоугольник. Цвет: {self.color}, ширина: {self.width} и он: {self.right}')

class Ellips(Figure):

    def draw(self):
        print(f'Рисуем эллипс. Цвет: {self.color} и ширина {self.width}')



f = Figure([1, 2, 3, 5, 8], 2, 'black')
f.draw()

l = Line([1,2,5,7], 5, 'Green')
l.draw()
l.del_line()

e = Ellips([1,5,2,7,3], 5, 'Blue')
e.draw()

r = Rect([1,8,6,2], 6, 'red', 'неправильный')
r.draw()
