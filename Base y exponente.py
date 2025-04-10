# siempre me gusta poner el import primero a mi
import pyfiglet
# primero definir la base y el exponente, tenemos que usar int, primero porque es un numero, esto no cuenta como string
Base = int(input("Escriba el numero que quieres usar de base :"))
Exponente = int(input("Escriba el numero que quieres usar como exponente :"))
# ocupamos el operador ( ** ) para decirle a python que calcule la base el numero de veces del exponente
Resultado = Base**Exponente

# Convertir el resultado a ASCII art, esto es extra solo para que se vea tuani en letras grandes
# le tengo que hacer una variable puesto a que no puedo printear el resultado de un solo, ya que es int, es necesario traducirlo a una string
# por eso antes de la variable es necesario ponerle todo en brackets y poner str y luego otros brackets para la variable, eso le indica a python convierta esa variable a una string
# todo esto se debe a que pyfiglet espera usar una string, y no sirve con int
# le pongo f antes de "" para convertirlo a una f-string, esto me permite usar una variable dentro de una string, ya le estoy diciendo que printee tambien el simbolo de igual (=)
ascii = pyfiglet.figlet_format(str(f"= {Resultado}"))
print(ascii)