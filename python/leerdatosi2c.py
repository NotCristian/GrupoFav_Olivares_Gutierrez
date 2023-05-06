import smbus
import time

bus = smbus.SMBus(1) # Crear un objeto SMBus para el bus I2C (el número 1 se refiere al bus I2C 1)
address = 0x04 # Dirección del dispositivo I2C

while True:
    	# Leer un byte de datos desde el dispositivo
	value = bus.read_byte(address)
   	# Mostrar el valor en la consola
	print(value)
	time.sleep(1)
