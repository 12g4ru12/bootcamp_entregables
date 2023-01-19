"""
En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto
de ella, lo guardaréis en un archivo y luego lo cargamos.
"""
import pickle

class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def atributes(self):
        print(f"color = {self.color} \nruedas = {self.ruedas} \npuertas = {self.puertas}")


v1 = Vehiculo("Rojo", 6, 4)

f = open('demovehiculo.bin', 'wb')
pickle.dump(v1, f)
f.close()

file = open('demovehiculo.bin', 'rb')
vehiculobin = pickle.load(file)
file.close()

print(vehiculobin.color)
print(vehiculobin.ruedas)
print(vehiculobin.puertas)
vehiculobin.atributes()
