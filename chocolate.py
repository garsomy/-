class Candy:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight



class Chocolate(Candy):

    def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
        super().__init__(name, price, weight)
        self.cocoa_percentage = cocoa_percentage
        self.chocolate_type = chocolate_type



class Gummy(Candy):

    def __init__(self, name, price, weight, flavor, shape):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.shape = shape



class HardCandy(Candy):

    def __init__(self, name, price, weight, flavor, filled):
        super().__init__(name, price, weight)
        self.flavor = flavor
        self.filled = filled






chocolate = Chocolate(name="Швейцарские луга", price=325.50, weight=220, cocoa_percentage=40, chocolate_type="молочный")
gummy = Gummy(name="Жуй-жуй", price=76.50, weight=50, flavor="вишня", shape="медведь")
hard_candy = HardCandy(name="Crazy Фрукт", price=35.50, weight=25, flavor="манго", filled=True)

print("Шоколадные конфеты:")
print(f"Название конфет: {chocolate.name}")
print(f"Стоимость: {chocolate.price} руб")
print(f"Вес брутто: {chocolate.weight} г")
print(f"Процент содержания какао: {chocolate.cocoa_percentage}")
print(f"Тип шоколада: {chocolate.chocolate_type}")
print("\nМармелад жевательный:")
print(f"Название конфет: {gummy.name}")
print(f"Стоимость: {gummy.price} руб")
print(f"Вес брутто: {gummy.weight} г")
print(f"Вкус: {gummy.flavor}")
print(f"Форма: {gummy.shape}")
print("\nФруктовые леденцы:")
print(f"Название конфет: {hard_candy.name}")
print(f"Стоимость: {hard_candy.price} руб")
print(f"Вес брутто: {hard_candy.weight} г")
print(f"Вкус: {hard_candy.flavor}")
print(f"Начинка: {hard_candy.filled}")
