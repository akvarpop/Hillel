# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
data = {
    'colors': ['red', 'green', 'blue', 'purple'],
    'fruits': ['pineapple', 'orange', 'banana'],
    'clothes': ['coat', 'tshirt']
}
#
# Завдання: перебудувати словник (не створюючи новий) таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника.
#
# Підказки:
# * dict[key] = value
# * for key in dict
# * for value in dict[key]
#
from collections import defaultdict

data_change = defaultdict(list)

for key, values in data.items():
    for value in values:
        data_change[value].append(key)

print(data_change)
