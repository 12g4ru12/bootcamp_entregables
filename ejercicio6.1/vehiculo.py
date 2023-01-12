class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        print(f"El veiculo cuenta con los siguientes atributos: \ncolor = {self.color} \nruedas = {self.ruedas}" \
              f"\npuertas = {self.puertas}")


class Coche(Vehiculo):

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        super().__str__()
        print(f"velocidad = {self.velocidad}" \
              f"\ncilindrada = {self.cilindrada}")


x = Coche("blanco", 4, 4, "250 km/h", 2.0)
x.__str__()

