# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
#
# підказка:
#  %= N  # compound assignment
N = int(input())
K = int(input())

if K > N:
    K %= N
    my_list = list(range(N))
    del my_list[K-1::K]
    print(my_list)
else:
    my_list = list(range(N))
    del my_list[K - 1::K]
    print(my_list)