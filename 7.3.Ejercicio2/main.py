import time as t

"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a 
casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación 
para calcular el tiempo que queda de trabajo.
"""

if __name__ == '__main__':

    fechaHora = t.strftime("%d/%m/%Y %H:%M", t.localtime())
    print(fechaHora)
    hora = t.localtime().tm_hour
    minutos = t.localtime().tm_min

    if hora < 19 and minutos <= 59:
        mensaje = "El tiempo que queda de trabajo es {} horas {} minutos"
        print(mensaje.format(abs(hora - 18), abs(minutos - 59)))
    else:
        print("No es hora laboral")

