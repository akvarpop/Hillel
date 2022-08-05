# Згенерувати, за допомогою list comprehension, послідовність
# цілих чисел 0..N де будуть відсутні кожний  K-ий елемент
#
# N, K запитати у користувача
# K повинно бути менша за N (строго), дозволити ввод К більшого
# за N але відмасштабувати його до розмірів менших за N (%)
#
# підказка:
#  %= N  # compound assignment

# # Вариант 1
# N = int(input())
# K = int(input())
#
#
# if K > N:
#      K %= N
#
# new_list = [K for K in range(0, N, K)]
#
# print(new_list)

# Вариант 2

N = int(input('Ввести значення N: '))
K = int(input('Ввести значення K: '))

if K > N:
    K = N % K

my_list = [i for i in range(N+1)]
del my_list[::K]

print(my_list)

# Мой первый вариант(без листа)


# if K > N:
#     K %= N
#     my_list = list(range(N))
#     del my_list[K-1::K]
#     print(my_list)
# else:
#     my_list = list(range(N))
#     del my_list[K - 1::K]
#     print(my_list)