def pedir_entero_positivo():
    while True:
        entrada = input("¿Cuántos números de la serie de Fibonacci deseas ver? ")
        try:
            n = int(entrada)
            if n <= 0:
                print("Por favor, ingresa un número entero positivo.")
            else:
                return n
        except ValueError:
            print("Entrada inválida. Ingresa solo un número entero positivo.")

n = pedir_entero_positivo()
a, b = 0, 1

print("Serie de Fibonacci:")

for _ in range(n):
    print(a)
    a, b = b, a + b