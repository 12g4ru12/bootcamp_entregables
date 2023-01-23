"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista
pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
from functools import reduce

numbersList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def oddnumber(x):
    if x % 2 != 0:
        return True

    return False


def summation(a, b):
    return a + b


oddNumberslist = list(filter(oddnumber, numbersList))
oddNumberResult = reduce(summation, oddNumberslist)

print(oddNumberResult)
