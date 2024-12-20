def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, list): # Проверка, является ли текущий элемент списком
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для каждого элемента списка
    elif isinstance(data, dict): # Проверка является  текущий элемент словарем
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Рекурсивный вызов для ключей
            total_sum += calculate_structure_sum(value)  # Рекурсивный вызов для значений
    elif isinstance(data, tuple): # Проверка является  текущий элемент кортежем
        for item in data:
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов для каждого элемента кортежа
    elif isinstance(data, (int, float)): # Если это число, добавляем его к сумме
        total_sum += data
    elif isinstance(data, str): # Если это строка, добавляем её длину к сумме
        total_sum += len(data)
    return total_sum
data_structure = [ # Пример использования функции
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)