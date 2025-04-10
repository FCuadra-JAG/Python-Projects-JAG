#15. Algoritmo que calcule el salario de un trabajador de la manera siguiente. 
#El trabajador cobra un precio fijo por hora y se le descuento el 5% en concepto de impuesto sobre la renta.
#El programa debe pedir el nombre del trabajador, las horas trabajadas y el precio que cobra por hora. 
#Como salida debe imprimir el nombre del trabajador, el sueldo bruto, el descuento de renta y el salario a paga.

nombre=input("Ingrese el nombre del trabajador")
horas_trabajadas=int(input("Ingrese las horas trabajadas"))
pago_por_hora=float(input("Ingrese su salario por hora"))

sueldo_bruto=horas_trabajadas*pago_por_hora
descuento=sueldo_bruto*0.05
sueldo_neto=sueldo_bruto-descuento

print("Nombre del trabajador ", nombre)
print("El sueldo bruto es de: ", "C$",sueldo_bruto)
print("Descuento por la renta: ", "C$",descuento)
print("Su salario menos el descuneto es de:", "C$",sueldo_neto)