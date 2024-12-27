class House:
    def __init__(self, name, number_of_floors=0):
        self.name = name  # Название ЖК
        self.number_of_floors = number_of_floors  # Количество этажей

    def setNewNumber_of_floors(self, floors): #Метод для изменения количества этажей
        self.number_of_floors = floors
        print(self.number_of_floors)

    def __eq__(self, other): #Метод сравнения на равенство (==)
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other): #Метод сравнения на меньше (<)
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other): #Метод сравнения на меньше или равно (<=)
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other): #Метод сравнения на больше (>)
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other): #Метод сравнения на больше или равно (>=)
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other): #Метод сравнения на неравенство (!=)
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value): #Метод сложения для увеличения этажей (+)
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        return NotImplemented

    def __radd__(self, value): #Метод обратного сложения (слева от +)
        return self.__add__(value)  # Используем логику __add__

    def __iadd__(self, value): #Метод сложения с присваиванием (+=)
        return self.__add__(value)  # Используем логику __add__

    def __str__(self): #Метод строкового представления объекта
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Пример использования класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Метрополия', 24)

print(h1)
print(h2)

# Сравнение на равенство
print(h1 == h2)  # Вывод: False

# Увеличение количества этажей
h1 = h1 + 10
print(h1)  # Вывод: Название: ЖК Эльбрус, кол-во этажей: 20

# Сравнение на равенство после увеличения этажей
print(h1 == h2)  # Вывод: True

# Увеличение количества этажей с помощью +=
h1 += 10
print(h1)  # Вывод: Название: ЖК Эльбрус, кол-во этажей: 30

# Увеличение количества этажей с помощью обратного сложения
h2 = 10 + h2
print(h2)  # Вывод: Название: ЖК Акация, кол-во этажей: 30

# Сравнение на больше
print(h1 > h2)  # Вывод: False

# Сравнение на больше или равно
print(h1 >= h2)  # Вывод: True

# Сравнение на меньше
print(h1 < h2)  # Вывод: False

# Сравнение на меньше или равно
print(h1 <= h2)  # Вывод: True

# Сравнение на неравенство
print(h1 != h2)  # Вывод: False