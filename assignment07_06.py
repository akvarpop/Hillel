"""Задача: написати функцію пошуку елемента у послідовності.

   Деталі:
            * функція приймає два аргумента - послідовність та елемен
            * функція повинна повернути індекс елемента у послідовності
              або -1 якщо не знайдено
            * це аналог функції str.find, list.index
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * search_linearly([1, 8, 7, 33, 9, 2], 8) -> повертає 1
            * search_linearly("hello world!", "!") -> повертає 11
            * search_linearly(tuple(range(10)), 10) -> повертає -1
"""

def search_linearly(my_list, my_index):
    if my_index not in my_list:
        return -1
    else:
        return my_list.index(my_index)


def my_func():
    list = [x for x in range(2, 20, 2)]
    return list


def my_func_2(start, step, stop):
    list2 = [i for i in range(start, step, stop)]
    return list2


print(search_linearly([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 30))
print(search_linearly("hello world!", "!"))
print(search_linearly(tuple(range(10)), 10))
print(search_linearly((1, 3, 33), 1))