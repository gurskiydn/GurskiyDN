def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    for word in other_words:# Перебираем все слова из других слов
        if word.startswith(root_word):# Проверка, начинается ли текущее слово с корневого слова
            same_words.append(word)  # Если да, добавляем его в список
    return same_words  # Вставляем в список подходящих слов
# Вызов функции и вывод результата
result = single_root_words('программ', 'программирование', 'программный', 'программа', 'документ')
print(result)