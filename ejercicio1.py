#Crear un programa que calcule la nota final de una asignatura. El sistema de evaluación incluye tres parciales, cada uno con una calificación de 0 a 100. 
# Para cada parcial, se realizan varias evaluaciones, cuyo promedio determina la nota del parcial. La nota final se obtiene promediando las calificaciones de los tres parciales.

def obtener_notas_parcial(parcial_num):
    while True:
        try:
            num_evaluaciones = int(input(f"Ingrese el número de evaluaciones del Parcial {parcial_num}: "))
            if num_evaluaciones <= 0:
                print("Debe haber al menos una evaluación.")
                continue

            notas = []
            for i in range(num_evaluaciones):
                nota = int(input(f"Ingrese la nota {i + 1} del Parcial {parcial_num} (0 a 100): "))
                if nota < 0 or nota > 100:
                    raise ValueError("La nota debe estar entre 0 y 100.")
                notas.append(nota)

            promedio_parcial = sum(notas) / len(notas)
            print(f"Promedio del Parcial {parcial_num}: {promedio_parcial:.2f}")
            return promedio_parcial

        except ValueError as e:
            print(f"Entrada inválida: {e}. Inténtelo de nuevo.")

def calcular_nota_final():
    print("Cálculo de la Nota Final")
    parciales = []
    for i in range(1, 4):
        promedio = obtener_notas_parcial(i)
        parciales.append(promedio)

    nota_final = sum(parciales) / 3
    print(f"\nLa nota final de la asignatura es: {nota_final:.2f}")

# Ejecutar el programa
calcular_nota_final()
