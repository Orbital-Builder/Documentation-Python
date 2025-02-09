# Exercice 1: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne la somme de ces nombres.
def sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


print(sum([1, 2, 3]))  # 6


# Exercice 2: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le maximum de ces nombres.
def max(numbers):
    result = numbers[0]
    for number in numbers:
        if number > result:
            result = number
    return result


print(max([1, 2, 3]))  # 3


# Exercice 3: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le minimum de ces nombres.
def min(numbers):
    result = numbers[0]
    for number in numbers:
        if number < result:
            result = number
    return result


print(min([1, 2, 3]))  # 1


# Exercice 4: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne la moyenne de ces nombres.

def average(numbers):
    result = 0
    for number in numbers:
        result += number
    return result / len(numbers)


print(average([1, 2, 3]))  # 2.0


# Exercice 5: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne la médiane de ces nombres.
def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    else:
        return numbers[n // 2]


print(median([1, 2, 3]))  # 2


# Exercice 6: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le nombre de nombres pairs dans cette liste.
def count_even(numbers):
    result = 0
    for number in numbers:
        if number % 2 == 0:
            result += 1
    return result


print(count_even([1, 2, 3]))  # 1


# Exercice 7: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le nombre de nombres impairs dans cette liste.

def count_odd(numbers):
    result = 0
    for number in numbers:
        if number % 2 != 0:
            result += 1
    return result


print(count_odd([1, 2, 3]))  # 2


# Exercice 8: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le nombre de nombres premiers dans cette liste.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def count_primes(numbers):
    result = 0
    for number in numbers:
        if is_prime(number):
            result += 1
    return result


print(count_primes([1, 2, 3]))  # 1


# Exercice 9: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le nombre de nombres pairs et impairs dans cette liste.

def count_even_odd(numbers):
    even = 0
    odd = 0
    for number in numbers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


print(count_even_odd([1, 2, 3]))  # (1, 2)


# Exercice 10: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne le nombre de nombres positifs, négatifs et nuls dans cette liste.

def count_positive_negative_zero(numbers):
    positive = 0
    negative = 0
    zero = 0
    for number in numbers:
        if number > 0:
            positive += 1
        elif number < 0:
            negative += 1
        else:
            zero += 1
    return positive, negative, zero


print(count_positive_negative_zero([1, -2, 0]))  # (1, 1, 1)


# Exercice 11: Écrire une fonction qui prend en paramètre une liste de nombres et qui retourne la somme, le maximum, le minimum, la moyenne, la médiane, le nombre de nombres pairs, le nombre de nombres impairs, le nombre de nombres premiers, le nombre de nombres positifs, négatifs et nuls dans cette liste.

def stats(numbers):
    return sum(numbers), max(numbers), min(numbers), average(numbers), median(numbers), count_even(numbers), count_odd(
        numbers), count_primes(numbers), count_positive_negative_zero(numbers)


print(stats([1, 2, 3]))  # (6, 3, 1, 2.0, 2, 1, 2, 1, 1, 1, 1)


#Fin Exercice