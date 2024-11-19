print("Введите 3 числа")
first = input("первое число: ")
second = input("второе число: ")
third = input("третье число: ")
if first == second and second == third:
    print("Одинаковых чисел - 3")
elif first == second or second == third or first == third:
    print("Одинаковых чисел - 2")
else:
    print("Нет одинаковых чисел  (их- 0)")
