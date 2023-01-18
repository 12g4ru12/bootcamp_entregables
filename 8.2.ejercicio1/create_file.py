"""
En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
Solución
"""

f = open('demofile.txt', 'w', encoding='utf-8')

title = "Escribir archibos en Python\n"
message = "Escribiendo dentro del archivo creado en python\n"

f.write(title)
f.write(message)

f.close()

f = open('demofile.txt', 'r', encoding='utf-8')
data = f.read()
print(data)

f.close()
