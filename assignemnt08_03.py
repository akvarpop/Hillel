# Завдання: замінити виклик своєї функції (ітерації та фільтрування елеменів)
#           на використання вбудованої функції filter (використати звичайну
#           або lambda функції як фільтруючу - перший аргумент).
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказки:
#    * filter(callable, iterable)
#

import random

my_list = [i for i in range(random.randint(int(input()), int(input())))]


def callable(element):
    if(element % 2) == 0:
        return True
    else:
        return False


print("List result: ", list(filter(callable, my_list)))