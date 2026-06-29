# Juego Adivina el Númeromayor
"""
La búsqueda binaria divide el rango de búsqueda 
en dos partes después de cada respuesta. 
Esto reduce la cantidad de intentos necesarios.
"""


minimo = 1
maximo = 100
intentos = 0

print("Piensa un número entre 1 y 100.")

while True:

    medio = (minimo + maximo) // 2
    intentos += 1

    respuesta = input(
        f"¿Tu número es {medio}? (mayor/menor/igual): "
    ).lower()

    if respuesta == "igual":
        print(f"Adiviné tu número en {intentos} intentos.")
        break

    elif respuesta == "mayor":
        minimo = medio + 1

    elif respuesta == "menor":
        maximo = medio - 1

    else:
        print("Respuesta inválida.")

    # Validación de respuestas contradictorias
    if minimo > maximo:
        print("Las respuestas ingresadas son inconsistentes.")
        break