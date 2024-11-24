grades = [[5,3,3,5,4], [2,2,2,3],[4,5,5,2], [4,4,3],[5,5,5,4,5]] # Оценки
students = {"Johnny", "Bilbo", "Sttvt", "Kendrik", "Aaron"}
sorted_students = sorted(students) # выставляем по алфавиту
print(sorted_students) # проверка по студентам
avereges_list = [sum(sublist) / len(sublist) for sublist in grades] # используем списковые включения  для создания
# нового списка. Для каждого подсписка вычисляется новое значение.
print(avereges_list) #выводим новый список на экран
rezult_dict = dict(zip(sorted_students, avereges_list)) # с помощью zip объединям два списка и преобразуем в словарь
print(rezult_dict) #вывод на экран