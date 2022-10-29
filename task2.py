import re
from collections import Counter
from fractions import Fraction
import sys

# Решение согласно уроку
def get_count_char(str_):
    prepared = str_.lower().replace('\n', ' ').replace(' ', '')
    counted = {letter: 0 for letter in prepared if letter.isalpha() is True}
    for letter in prepared:
        if letter in counted:
            counted[letter] += 1

    return counted

# Мое решение
def get_count_char_new(str_):
    prepared = re.sub(r'[^\w]', '', str_.lower())
    counted = Counter(prepared)

    return dict(counted) # можно вернуть и объектом Counter, манипуляции почти идентичны как и со словарем

def proportion(dict_):
    overall = sum(dict_.values())
    recalculated = {key: round(value * 100 / overall, 2) for key, value in dict_.items()}
    # recalculated = {key: Fraction(value, overall) for key, value in dict_.items()} Интерпретация с дробями вместо чисел с плавающей точкой, assert точно будет проходить

    assert (100 - sum(recalculated.values()) <= sys.float_info.epsilon), f'Ожидалось 100, но получено {sum(recalculated.values())}' # проверка стремления 

    return recalculated


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

count_words = get_count_char_new(main_str)
recalculated = proportion(count_words)

print(count_words)
print(recalculated)