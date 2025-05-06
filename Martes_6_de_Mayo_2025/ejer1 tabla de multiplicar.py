#Ejercicio 1: Tabla de multiplicar de un número
#Tipo de bucle: para
#Enunciado: Pide al usuario un número entero positivo y muestra su tabla de multiplicar del 1 al 10.
#Procedimiento paso a paso:
#1.	Solicita al usuario un número entero positivo.
#2.	Usa un bucle para que vaya de 1 a 10.
#3.	En cada iteración, multiplica el número ingresado por el número de la iteración.
#4.	Muestra el resultado en cada paso en pantalla.


# Solicita al usuario un número entero positivo
while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero > 0:
            break
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número entero.")

# Usa un bucle para que vaya de 1 a 10
print(f"\nTabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
