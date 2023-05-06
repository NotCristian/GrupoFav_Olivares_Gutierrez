import serial

# Configuración de la comunicación serial
ser = serial.Serial('/dev/ttyACM0', 9600) # Se utiliza el puerto serial /dev/ttyACM0 a una velocidad de 9600 baudios

while True:
    # Leer datos desde Arduino
	line = ser.readline().decode('utf-8').strip()
	print(line)
