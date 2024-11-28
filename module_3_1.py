calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls() #Увеличиваем счетчик
    lenght = len (string)
    upper  = string.upper()
    lower = string.lower()
    return  (lenght, upper, lower)

def is_contains(string, list_to_search):
    count_calls() # Увеличили счетчик
    lower_string = string.lower()                            # Приводим строку к нижнему регистру для сравнения.
    return lower_string in (item.lower() for item in list_to_search) # Проверяем, содержится ли строка в списке.
# Проверяем
my_string = string_info("HellO")
print(my_string)
resul_1 = is_contains("WorlD", ["hello", "worlld", "python"])
print(resul_1)
print(calls)

