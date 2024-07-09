"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    [1, 4, 25, 49]
    """

    return list(map(lambda arg: arg ** 2, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(numb):
    if numb < 2:
        return False
    for indx in range(2, int((numb ** 0.5)) + 1):
        if numb % indx == 0:
            return False
    return True

def is_odd (numb):
    return True if numb % 2 > 0 else False

def is_even (numb):
    return True if numb % 2 == 0 else False

funcs = {ODD: is_odd, EVEN: is_even, PRIME: is_prime}

def filter_numbers(numbers, operation):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    [2, 4]
    >>> filter_numbers([0, 1, 2, 3,4,5,6,7,8,9,10,11], PRIME)
    [2, 3, 5, 7, 11]
    """

    return list(filter(funcs[operation], numbers))

