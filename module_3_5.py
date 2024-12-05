def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    first = int(str_number[0])  # Берем первую цифру и преобразуем в целое число

    if len(str_number) > 1:  # Проверяем, больше ли длина строки 1
        return first * get_multiplied_digits(
            int(str_number[1:]))  # Умножаем первую цифру на результат рекурсии
    else:
        return first  # Если длина строки не больше 1, возвращаем первую цифру

result = get_multiplied_digits(21112)# Пример
print(result)