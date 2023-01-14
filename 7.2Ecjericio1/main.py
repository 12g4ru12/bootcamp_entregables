from basic_calculator_operations import basic_operations as bo

"""
En este example tendréis que crear un módulo que contenga las operaciones básicas
de una calculadora: sumar, restar, multiplicar y dividir.
Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas.
Los resultados tenéis que mostrarlos por consola.
"""

if __name__ == '__main__':
    print("Suma :", bo.suma(3, 15))
    print("Resta: ", bo.resta(4, 2))
    print("Multiplicacion :", bo.multiplicacion(8, 7))
    print("Division :", bo.division(50, 5))
