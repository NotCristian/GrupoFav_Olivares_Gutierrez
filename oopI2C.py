import time
import smbus

bus = smbus.SMBus(1) # Crear un objeto SMBus para el bus I2C (el número 1 se refiere al bus I2C 1)
address = 0x04 # Dirección del dispositivo I2C

class ArduinoI2C():

    def __init__(self):
        self.ard = smbus.SMBus(1)
    def leerI2C(self,address):
        return self.ard.read_byte(address)


Arduino = ArduinoI2C()
while True:
    	# Leer un byte de datos desde el dispositivo
	value = Arduino.leerI2C(address)
   	# Mostrar el valor en la consola
	print(value)
	time.sleep(1)
