ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(numbers, operation):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    def is_prime(x):
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                return False
        return True

    if operation == EVEN:
        return (list(number for number in numbers if number % 2 == 0))
    if operation == ODD:
        return (list(number for number in numbers if number % 2 > 0))
    if operation == PRIME:
        return (list(number for number in numbers if is_prime(number)))



print (25 if 2 == 1 else 24)

print(filter_numbers([1, 2, 3], ODD))

print(filter_numbers([2, 3, 4, 5], EVEN))

print(filter_numbers([2, 3, 4, 5], PRIME))

