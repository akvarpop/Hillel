# Завдання: модіфікувати попередне завдання використавши
#          lambda функції.
#
# Приклад:
#         ввод: 32 7 0 10 11 78 9 5 23 99
#         результат: 32 0 10 78
#
# Підказка:
#   * evens = lambda n: n % 2 == 0 (чи можно одразу передати
#                lambda n: n % 2 == 0 у місці виклиу функції
#                другим аргументом - вона одразу присвоїться
#                в аргумент, але не буде доступна після).


import random

my_list = [i for i in range(random.randint(int(input()), int(input())))]

rule = lambda element: True if (element % 2) == 0 else False

print("List result: ", list(filter(rule, my_list)))
