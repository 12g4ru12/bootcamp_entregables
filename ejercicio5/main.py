"""
Año bisiesto

CRITERIOS
El año se puede dividir uniformemente por 4, es un año bisiesto, a menos que:
El año se puede dividir uniformemente por 100, NO es un año bisiesto, a menos que:
El año también es divisible por 400. Entonces es un año bisiesto.
"""


def isleap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


print("Es un año bisiesto:", isleap(2023))
