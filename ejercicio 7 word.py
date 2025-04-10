#7. Calcula la calificación final de un estudiante con ponderaciones:
#Tareas: 30%
#Examen parcial: 30%
#Examen final: 40%
print("Ingrese a continuacion las califiaciones del estudiante de 0-100")
calificacion_tarea=float(input("Ingrese la calificasion de las tareas"))
calificacion_examen_parcial=float(input("Ingrese la calificasion del examen parcial"))
calificacion_examen_final=float(input("Ingrese la calificasion del examen final"))

calificaion_final=(calificacion_tarea * 0.30 )+(calificacion_examen_parcial * 0.30)+(calificacion_examen_final * 0.40)

print("La calificacion final del estudiante es de: " , calificaion_final)