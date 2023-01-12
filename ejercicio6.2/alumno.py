class Alumno:

    def __init__(self, nombreCompleto, nota):
        self.nombreCompleto = nombreCompleto
        self.nota = nota

    def analizarNota(self):
        if 3.0 <= self.nota <= 5.0:
            print(f"Nombre del studiante = {self.nombreCompleto} \nNota = {self.nota} Aprobó")
        elif 0.0 <= self.nota <= 2.9:
            print(f"Nombre del studiante = {self.nombreCompleto} \nNota = {self.nota} Reprobó")
        else:
            print("La nota no está en el rango requerido para la calificación")


estudiante = Alumno("Abraham García", 5)
estudiante.analizarNota()
