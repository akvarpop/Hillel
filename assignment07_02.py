# Згенерувати, за допомогою list comprehension,
# квадратну диагональну матрицю завданої розмірності (N)
# N - запитати у користувача
#
# Приклад:
# N = 4
#
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
#
# підказка: j+1 if i = j else 0

size = int(input('Введите размер матрицы: '))
# for row in range(size):
#     for col in range(size):
#         if row == col:
#             print(row + 1, end=' ')
#         else:
#             print(0, end=' ')
#     print()
#
matrix = [[i+1 if i == j else 0 for i in range(size)] for j in range(size)]

print(matrix)


