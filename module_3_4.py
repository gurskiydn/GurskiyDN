def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для подходящих слов
    root_word_lower = root_word.lower()
    for word in other_words:# Перебираем все слова из других слов
        word_lower = word.lower()
        if root_word_lower in word_lower and word_lower.count (root_word_lower) == 1:
            same_words.append(word)  #  добавляем его в список
    return same_words  # Вставляем в список подходящих слов
# Вызов функции и вывод результата
result = single_root_words('Программ', 'программирование', 'программный', 'Программа', 'документ')
print(result)