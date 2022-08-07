# Завдання: написати програму обчислення факторіалу числа.
#           Программа запитує ввод від користувача у циклі
#           (вихід можливий за допомогою Ctrl-C/D)
# 
# Факторіал числа: n!
# n! = 1 * 2 * 3 * 4 ... n-1 * n
# 0! = 1
#
# Приклад роботи:
#
# Введіть число для обчислення факторіалу: 5
# 5! == 120
# 
# Введіть число для обчислення факторіалу: -5
# Невірний ввод
# def factorial(n):
# 	result = 1
# 	for i in range(1,n+1):
# 		result = result*i
# 	return result
#
# n = int(input('Введіть число для обчислення факторіалу: '))
# result = factorial(n)
# print(n,'! == ',result,sep="")

# Вариант_1

def factorial(n):
	result = 1
	i=1
	while i<=n:
		result*=i
		i+=1
	return result

n = int(input('Введіть число для обчислення факторіалу: '))
if n < 0:
	print("Невірний ввод")
else:
	result = factorial(n)
	print(n,'! == ',result,sep="")

# Вариант_2

# num = int(input('Ввести число: '))
#
#
# def my_func(n):
#     factorial = 1
#     for i in range(2, n + 1):
#         factorial *= i
#     return factorial
#
# if num >= 0:
#     print(my_func(num))
# else:
#     print('Невірний ввод')



