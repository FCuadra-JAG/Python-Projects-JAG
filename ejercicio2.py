#Elabore un programa que solicite, por separado, su nombre y apellido. Como resultado deberá presentar la inicial del nombre, seguido el apellido.

def es_string_valido(texto):
    return texto.isalpha()

def obtener_nombre_apellido():
    while True:
        nombre = input("Ingrese su nombre: ").strip()
        if not es_string_valido(nombre):
            print("El nombre solo debe contener letras. Intente nuevamente.")
            continue
        
        apellido = input("Ingrese su apellido: ").strip()
        if not es_string_valido(apellido):
            print("El apellido solo debe contener letras. Intente nuevamente.")
            continue

        inicial = nombre[0].upper()
        apellido_formateado = apellido.capitalize()
        print(f"Resultado: {inicial}. {apellido_formateado}")
        break

# Ejecutar el programa
obtener_nombre_apellido()
