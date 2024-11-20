def get_matrix(n, m, value):
    matrix = []

    for i in range(n):  # Внешний цикл для создания строк матрицы
        row = []  # Создаем пустую строку

        for j in range(m):  # Внутренний цикл для заполнения столбцов значениями
            row.append(value)  # Добавляем значение в строку

        matrix.append(row)  # Добавляем заполненную строку в матрицу
    return matrix  # Возвращаем созданную матрицу
n = int(input("vvod str :", ))  # Ввод кол-ва строк
m = int(input("vvod stolb : ", ))  # Ввод кол-ва столбцов
value = int(input("vvod chsla : ", ))  # Ввод числа
result = get_matrix(n, m, value)
print(result)
