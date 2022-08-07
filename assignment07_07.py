"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""
import random


def lite_сalculator(left_operand, operator, right_operand):
    if operator == "+":
        return left_operand + right_operand
    elif operator == "-":
        return left_operand - right_operand
    elif operator == "*":
        return left_operand * right_operand
    elif operator == "/":
        return left_operand / right_operand
    else:
        return


def my_func_for_int(a, b):
    return random.randint(a, b)


def my_func_for_str(s):
    return s * 2


def my_func_for_operator(s2):
    if len(s2) > 0:
        return "*"


print(lite_сalculator(2, "+", 2))
print(lite_сalculator("hello world!", "*", 2))
print(lite_сalculator(10, ")", 10))
print(lite_сalculator(10, "/", 2))
