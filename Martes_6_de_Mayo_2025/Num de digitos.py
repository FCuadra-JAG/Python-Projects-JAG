def pedir_numero_positivo():
    while True:
        entrada = input("Ingresa un número entero positivo: ")
        try:
            numero = int(entrada)
            if numero <= 0:
                print("El número debe ser mayor que cero.")
            else:
                return numero
        except ValueError:
            print("Entrada inválida. Ingresa un número entero positivo.")

numero = pedir_numero_positivo()
conteo = 0

while numero > 0:
    numero //= 10
    conteo += 1

print(f"El número tiene {conteo} dígito(s).")