"""
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar
en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista
de países ordenados alfabéticamente y separados por comas.
"""

countries = input("Por favor escriba una lista de paises separada por espacios: ")  # Entrada de usuario
countrySet = set(countries.split())  # Los sets eliminan los paises repetidos
countryList = list(countrySet)  # Se pasa a una lista para utilizar el metodo sort() para organizar alfabéticamente
countryList.sort()

print(countryList)
