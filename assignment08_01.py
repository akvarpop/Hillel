# Завдання: написати функцію фільтрації послідовності відповідно до умови.
#           Функція приймає два аргумента:
#              * послідовність (list, str, tuple - не важливо, щось що можно
#                               ітерувати - iterable)
#              * функцію умови (callable - щось що можно визвати як функцію
#                               callable(element) результатом буде True чи False)
#           Повертаєме значення: список елементів для яких callable(element)
#                                повертає True (задовольняють умові callable)
#
#           Використати написану функцію щоб обрати з послідовності
#           усі числа які поділяються на два. Послідовність чисел
#           запитати у користувача або згенерувати рандомно (довільну кількість).
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказки:
#    * list comprehension [arg2(i) for i in iterable]
#    * def function_name(arg1, arg2):
#    * function_name(arg1, arg2)
#    * arg2 - це ім'я функції (спосіб передачі у вигляді аргументу)

import random

my_list = [i for i in range(random.randint(int(input()), int(input())))]


def callable(element):
    if(element % 2) == 0:
        return True
    else:
        return False


out_filter = filter(callable, my_list)

print("List result:", list(out_filter))