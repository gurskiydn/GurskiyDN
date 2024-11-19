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
for j in numbers:  # исправил
    if is_prime(j):
        primes.append(j)
    elif j >= 2:  # Число больше 1. 1 и не простое и не сложное
        not_primess.append(j)

# Распечатка
print("Primes: ", primes)
print("Not Primes: ", not_primess)
