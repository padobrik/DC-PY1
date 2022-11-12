import random

def get_unique_list_numbers() -> list[int]:
    unique_numbers = []
    while len(unique_numbers) < 15:
        number = random.randint(-10, 10) # в случае функции randint() обе границы включаются в диапазон
        if number in unique_numbers:
            continue
        unique_numbers.append(number)

    return unique_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))