# declaramos las variables
monto_prestamo =10000.00  # Monto del préstamo recibido en pesos
print("el monto del prestamo fue de", monto_prestamo, "con un interes anual del 27%")
tasa_interes_anual = 0.27  # Tasa de interés anual expresada como decimal (27% = 0.27)
tiempo_años = int(input("Cuantos años han pasado desde el prestamo: "))  # Tiempo del préstamo en años

#Calculamos el interes
# Fórmula: Interés = Principal * Tasa * Tiempo
# El operador * se utiliza para multiplicar valores
interes_pagado = monto_prestamo * tasa_interes_anual * tiempo_años

# Usamos print() para mostrar al usuario cuánto pagará de interés
print(f"El interés a pagar después de {tiempo_años} año(s) será de ${interes_pagado:.2f}")
#interes_pagado: es la variable que queremos mostrar (por ejemplo, 2700.0).
# : esto indica que vamos a aplicar un formato especial al número.
#.2f:
# El .2 significa que se mostrarán 2 decimales.
# La f indica que es un número de tipo float (decimal).