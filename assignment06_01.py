# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.
#
# Підказки:
# * input
# * str.split
# * for word in sequence
# * if key in dict
# * if key not in dict

import pandas as pd # как вариант но без словаря

text_input = str(input('Введіть текст:'))
text_input_split = str.split(text_input)
count_all_words = len(text_input_split)

count_words = {}
for key in text_input_split:
    count_words[key] = count_words.setdefault(key, 0) + 1

count_symbols = dict.fromkeys(text_input, 0)
for c in text_input: count_symbols[c] += 1

print(f"Кількість слів у реченні:{count_all_words}")
print(f"Кількість разів воно зустрічається у реченні: {count_words}")
print(count_symbols)
print(pd.Series(list(text_input)).value_counts()) # как вариант но без словаря
