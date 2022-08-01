# Завдання: додати умову яка б допомогала запобігати доступ до неіснуючого ключа у словнику.
#
# Словник з числами генерується з рандомною кількістю елементів (від 1 до 100), кожний
# елемент має ключ - порядковий номер, та значення "item_{порядковий номер}". Далі
# код програми намагється напечатати елемент по 66-му ключу, який може бути присутній
# або відсутній - у разі відсутності скрипт завершиться з помилкою KeyError (для того
# щоб відтворити помилку може знадобитись декілька пусків скрипта поки згенерований
# словник не буде містити елемент з ключем 66. Потрібно додати логіку перевірки наявності
# ключа та надати його значення чи, у разі відсутності, надати інформацію що елемент з
# таким ключем - відсутній).
#
# Приклад роботи (два запуска скрипта, 1-й коли ключ присутній, 2-й ключ відсутній):
#
#     Елемент 66: item_66.
#     Помилка: елемент з ключем 66 відсутній.
#
# Підказка: у випадку відсутнього ключа, номер елементу не повинен бути захардкодженим
#           у текстовий літерал, та повинен буди підставлений через форматну строку зі
#           змінної.
import random  # модуль з функціями генерації випадкових чисел

search_key = 66

data = {}
# генеруємо рандомне число від 1 до 100, а потім створюємо послідовність від 0 до сгенерованого числа
for i in range(random.randint(1, 100)):
    data[i] = f"item_{i}"  # наповнюємо словник відповідно до послідовності рандомної довжини
if i >= search_key:
    print(f"Елемент {search_key}: {data[search_key]}")
else:
    print('Елемент з таким ключем - відсутній')

# d = {"key1": 10, "key2": 23}
#
# if "key1" in d:
#     print("this will execute")
#
# if "nonexistent key" in d:
#     print("this will not")


# print(data)
# print(f'Number{i}')

