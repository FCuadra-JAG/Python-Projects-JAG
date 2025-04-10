# primero definimos los numeros
Num1 = int(input("Numero 1 : "))
Num2 = int(input("Numero 2 : "))
# le hacemos una variable al conjunto de estos dos numeros
X, Y = Num1, Num2
print(X, Y)
# le decimos a python que esa variable es lo mismo que lo contrario
X, Y = Y, X
# Cuando Printea por segunda vez usa el nuevo valor, dandonos el intercambio de valores
print(X, Y)