from collections import Counter
from decimal import Decimal, getcontext
from math import log
from math import ceil


def arithmetic_encode_with_ranges(text, precision=50):
    getcontext().prec = precision

    freq = Counter(text)
    total = Decimal(len(text))

    prob = {char: Decimal(freq[char]) / total for char in freq}

    ranges = {}
    low = Decimal(0)
    for char, p in prob.items():
        high = low + p
        ranges[char] = {'low': low, 'high': high}
        low = high
    print("Диапазоны символов:")
    for char, p in prob.items():
        print(f"{char}: {ranges[char]['low']}, {ranges[char]['high']}")

    print("Процесс построения отрезков:")
    low, high = Decimal(0), Decimal(1)
    for char in text:
        difference = high - low
        difference = Decimal(difference)
        low = low + ranges[char]['low'] * difference
        high = low + difference * (ranges[char]['high'] - ranges[char]['low'])
        print(low, high)
    result_log = ceil(-log(high - low, 2))
    result = ceil(low * 2 ** result_log)

    return '0' * (result_log - len(bin(result)[2:])) + bin(result)[2:], ranges


def Arithmetic_encode(text):
    code_with_ranges, ranges_with_keys = arithmetic_encode_with_ranges(text)
    print("Итоговый код и его длина:")
    print(code_with_ranges, len(code_with_ranges))
    print(f"I(a) = {(len(code_with_ranges)) / len(text)}")


input_text = str(input("Введите слово (или слова без пробелов): "))
Arithmetic_encode(input_text)
