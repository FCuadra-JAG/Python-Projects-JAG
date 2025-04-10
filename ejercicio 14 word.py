#14. En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital se reparte de la siguiente manera:
#AREA               Presupuesto
#Urgencias              37%
#pediatria              42%
#traumatologia          21%

#Obtener la cantidad de dinero que recibirá cada área para cualquier monto presupuestal.

presupuesto_anual=float(input("Ingrese el presupuesto anual del hospital"))

Urgencias=presupuesto_anual*0.37
Pediatria=presupuesto_anual*0.42
Traumatologia=presupuesto_anual*0.21

print("El presupuesto anual del hospital se preparte entre las Areas de la seguiente manera: ")
print("Urgencias",Urgencias)
print("Pediatria",Pediatria)
print("Traumatologia",Traumatologia)

