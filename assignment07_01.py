# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
data = {
    'colors': ['red', 'green', 'blue', 'purple'],
    'fruits': ['pineapple', 'orange', 'banana'],
    'clothes': ['coat', 'tshirt']
}
#
# Завдання: перебудувати словник таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника. Вирішити за допомогою dict
#           comprehensions.


import pprint

pprint.pprint({i: k for k, v in data.items() for i in v})
