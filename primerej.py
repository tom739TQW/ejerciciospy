from datetime import datetime

nombre = input("¿Cómo te llamas? ")
print("¡Bienvenido/a,", nombre, "!")

ahora = datetime.now()
print("Fecha de ejecución:", ahora.strftime("%d/%m/%Y"))
print("Hora de ejecución:", ahora.strftime("%H:%M:%S"))