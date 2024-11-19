numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Проверка, является ли число простым
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Списки  простых и сложных чисел
primes = []
not_primess = []

# Цикл по числам
for j in range(len(numbers) + 1):  # не знаю по чему, но без +1 не выдает "15"
    if is_prime(j):
        primes.append(j)
    elif j > 1:  # Число больше 1 и не простое - сложное
        not_primess.append(j)

# Распечатка
print("Primes: ", primes)
print("Not Primes: ", not_primess)
