import random

numero_secreto = random.randint(1, 10)

def pedir_numero():
    while True:
        entrada = input("Adivina el número entre 1 y 10: ")
        if not entrada.isdigit():
            print("Entrada inválida. Ingresa solo números enteros positivos.")
            continue

        numero = int(entrada)
        if numero < 1 or numero > 10:
            print("El número debe estar entre 1 y 10.")
        else:
            return numero

intento = pedir_numero()

while intento != numero_secreto:
    if intento < numero_secreto:
        print("🔺 El número es mayor.")
    else:
        print("🔻 El número es menor.")
    intento = pedir_numero()

print("¡Felicidades! Has adivinado el número.")