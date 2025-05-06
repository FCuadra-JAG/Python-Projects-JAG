#Ejercicio 2: Contar números pares hasta un límite
#Tipo de bucle: mientras
#Enunciado: Solicita un número positivo y muestra todos los números pares desde 0 hasta ese número.
#Procedimiento paso a paso:
#1.	Solicita al usuario un número positivo.
#2.	Inicializa un contador en 0.
#3.	Utiliza un bucle mientras que se ejecute mientras el contador sea menor o igual al número ingresado.
#4.	En cada iteración, verifica si el contador es par.
#5.	Si es par, muestra el número.
#6.	Incrementa el contador en 1.


 #Solicita al usuario un número positivo
while True:
    try:
        limite = int(input("Introduce un número entero positivo: "))
        if limite >= 0:
            break
        else:
            print("El número debe ser positivo o cero.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número entero.")

#Inicializa un contador en 0
contador = 0

print(f"\nNúmeros pares desde 0 hasta {limite}:")

#Bucle mientras el contador sea menor o igual al número ingresado
while contador <= limite:
    # Verifica si el contador es par
    if contador % 2 == 0:
        
        print(contador)
    # Incrementa el contador en 1
    contador += 1
