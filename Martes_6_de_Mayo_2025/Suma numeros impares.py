contador = 1
suma = 0

while contador <= 100:
    if contador % 2 != 0:  # Verifica si el número es impar
        suma += contador
    contador += 1

print("La suma de los números impares del 1 al 100 es:", suma)