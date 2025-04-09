import pytz
from datetime import datetime 
# Tuve que instalar pip a python, esto se hace mediante la terminal/shell ya que no reconocia la bibliotecca pytz

# Zona horaria
zona = input("Ingresa tu zona horaria (ej. America/Managua): ")

try:
    tz = pytz.timezone(zona)

    # Solicitar fecha y hora de nacimiento
    nacimiento_str = input("Escribe la fecha y hora de nacimiento (formato: AAAA-MM-DD HH:MM): ")
    nacimiento = tz.localize(datetime.strptime(nacimiento_str, "%Y-%m-%d %H:%M"))

    # Obtener la hora actual en la zona especificada
    ahora = datetime.now(tz)

    # Calcular diferencia
    diferencia = ahora - nacimiento

    # Calcular años, meses, días, etc.
    total_segundos = diferencia.total_seconds()
    años = int(total_segundos // (365.25 * 24 * 3600))
    meses = int((total_segundos % (365.25 * 24 * 3600)) // (30.44 * 24 * 3600))
    dias = int((total_segundos % (30.44 * 24 * 3600)) // (24 * 3600))
    horas = int((total_segundos % (24 * 3600)) // 3600)
    minutos = int((total_segundos % 3600) // 60)

    print(f"Edad aproximada del individuo: {años} años, {meses} meses, {dias} días, {horas} horas y {minutos} minutos.")

except Exception as e:
    print("Ocurrió un error:", e)