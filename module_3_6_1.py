def calculate_structure_sum(data):
    total_sum = 0

    for element in data:
        if isinstance(element, (int, float)):  # Проверяем, является ли элемент числом
            total_sum += element
        elif isinstance(element, str):  # Проверяем, является ли элемент строкой
            total_sum += len(element)
        elif isinstance(element, list):  # Проверяем, является ли элемент списком
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для списка
        elif isinstance(element, dict):  # Проверяем, является ли элемент словарем
            total_sum += calculate_structure_sum(element.keys())  # Рекурсивный вызов для ключей
            total_sum += calculate_structure_sum(element.values())  # Рекурсивный вызов для значений
        elif isinstance(element, tuple):  # Проверяем, является ли элемент кортежем
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для кортежа
        elif isinstance(element, set):  # Проверяем, является ли элемент множеством
            total_sum += calculate_structure_sum(element)  # Рекурсивный вызов для множества

    return total_sum

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    {9, 10},
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99

print(result)  # Вывод: 99
