#Ejercicio 4: Contador regresivo
#Tipo de bucle: para
#Enunciado: Solicita al usuario un número positivo e imprime un conteo regresivo hasta 0.
#Procedimiento paso a paso:
#1.	Solicita un número entero positivo.
#2.	Usa un bucle para que comience desde el número ingresado y vaya disminuyendo hasta 0.
#3.	Muestra cada número en pantalla.


# Solicita un número entero positivo
while True:
    try:
        numero = int(input("Introduce un número entero positivo: "))
        if numero >= 0:
            break
        else:
            print("El número debe ser positivo.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número entero.")

#Usa un bucle para contar regresivamente hasta 0
print(f"\nConteo regresivo desde {numero} hasta 0:")
for i in range(numero, -1, -1):  # Empieza en 'numero', termina en 0 (inclusive), de uno en uno hacia atrás

    print(i)
