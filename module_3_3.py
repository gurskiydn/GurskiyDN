def print_params(a = 1, b = "строка", c = True):
    print (a, b, c) # вывод 3х аргументов
    print(a) #вывод 1 аргумента
    print(b,c) #вывод 2х аргументов
print_params() #вывод после вызова без указания аргументов
print_params(b = 25) #замена второго аргумента
print_params(c = [1,2,3]) #замена третьего аргумента

value_list = [33, "пример2", False] # создан список с 3 разными аргументами
value_dict = {"a":33,"b": "текст","c": False} #создаем словарь
print_params(*value_list) #передаем список
print_params(**value_dict) #передаем словарь
value_list_2 = [43, "строка3"] #создаем список из 2х элементов
print_params(*value_list_2,42) #заменили часть списка
