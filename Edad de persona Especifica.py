# Importamos la librería 'pytz' que nos permite trabajar con zonas horarias.
import pytz

# Importamos 'datetime' desde la librería estándar para trabajar con fechas y horas.
from datetime import datetime 
# Tuve que instalar pip a python, esto se hace mediante la terminal/shell ya que no reconocia la bibliotecca pytz de zonas horarias, ya que no viene instalado por defecto

# Zona horaria
# Pedimos al usuario que escriba su zona horaria (como 'America/Managua' o 'Europa/Madrid')
zona = input("Ingresa tu zona horaria (ej. America/Managua): ")

try:
     # Intentamos crear una variable de zona horaria con pytz usando lo que escribió el usuario.
    tz = pytz.timezone(zona)

    # Solicitar fecha y hora de nacimiento
    # El formato debe ser exacto: Año-Mes-Día Hora:Minuto (ej: 2000-05-10 13:30)
    nacimiento_str = input("Escribe la fecha y hora de nacimiento (formato: AAAA-MM-DD HH:MM): ")
    #la parte que dice datetime.strptime(nacimiento_str, "%Y-%m-%d %H:%M")
    # Convierte el texto que ingresó el usuario en un objeto de tipo datetime (fecha y hora)
    # El formato debe coincidir con el que se indica:
    # %Y = año con 4 dígitos, %m = mes, %d = día, %H = hora (24h), %M = minutos
    nacimiento = tz.localize(datetime.strptime(nacimiento_str, "%Y-%m-%d %H:%M")) 
    #la parte que dice tz.localize
    # Toma ese objeto datetime (que no tiene zona horaria) y le asigna la zona horaria indicada por el usuario
    # Esto es importante porque sin zona horaria, Python no puede saber en qué lugar del mundo ocurrió ese momento.

    # Obtener la hora actual en la zona especificada
    ahora = datetime.now(tz)

    # Calculamos la diferencia entre la hora actual y la fecha de nacimiento
    diferencia = ahora - nacimiento

   
    # Vamos a calcular la cantidad total de segundos que hay en esa diferencia
    total_segundos = diferencia.total_seconds()

    # Calcular años, meses, días, etc.
    # Calculamos años aproximados, usando el promedio de 365.25 días por año (incluyendo los bisiestos)
    años = int(total_segundos // (365.25 * 24 * 3600))
    
    # sacamos los meses, usando promedio de 30.44 días por mes
    # Usamos el módulo (%) para sacar lo que sobró después de contar años
    meses = int((total_segundos % (365.25 * 24 * 3600)) // (30.44 * 24 * 3600))

    # Calculamos días restantes (lo que sobró después de contar los meses)
    dias = int((total_segundos % (30.44 * 24 * 3600)) // (24 * 3600))

    # Calculamos horas restantes dentro del día
    horas = int((total_segundos % (24 * 3600)) // 3600)

    # sacamos los minutos restantes dentro de la última hora
    minutos = int((total_segundos % 3600) // 60)
    # Imprimimos la edad aproximada del usuario
    print(f"Edad aproximada del individuo: {años} años, {meses} meses, {dias} días, {horas} horas y {minutos} minutos.")

# Si en algún punto algo sale mal (por ejemplo, el formato está mal escrito), mostramos un mensaje de error.
except Exception as e:
    print("Ocurrió un error:", e)


#try/except: Esta estructura sirve para manejar errores. Si ocurre un problema dentro del bloque try, el programa no se rompe, sino que va al except y muestra un mensaje amigable.

#strptime: Convierte texto en una fecha. En este caso, espera que el usuario escriba la fecha con el formato exacto "YYYY-MM-DD HH:MM".

#localize: Esta función de pytz agrega la información de la zona horaria a una variable datetime.

#datetime.now(tz): Obtiene la hora actual, pero usando la zona horaria especificada.

#total_seconds(): Convierte la diferencia de tiempo en una cantidad de segundos. Desde ahí se puede calcular todo lo demás (años, meses, etc.).
