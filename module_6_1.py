class Animal:# Определяем родительский класс Animal
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name   # Имя животного
class Plant:# Определяем родительский класс Plant
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name     # Имя растения
class Mammal(Animal):# Класс Mammal наследует от Animal
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
class Predator(Animal):# Класс Predator наследует от Animal
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Flower(Plant):# Класс Flower наследует от Plant
    pass  # Цветы не съедобные по умолчанию


class Fruit(Plant):# Класс Fruit наследует от Plant
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты съедобные
# Создаем объекты классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
# Выводим имена животных и растений
print(a1.name)
print(p1.name)
# Проверяем состояние животных
print(a1.alive)
print(a2.fed)
# Хищник пытается съесть цветок
a1.eat(p1)
# Млекопитающее ест фрукт
a2.eat(p2)
# Проверяем состояние животных после еды
print(a1.alive)
print(a2.fed)
