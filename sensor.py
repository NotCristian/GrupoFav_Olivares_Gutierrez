import time
from datetime import datetime
from w1thermsensor import W1ThermSensor #Importamos el paquete W1ThermSensor

class ib1820():

    def __init__(self):
        self.sensor = W1ThermSensor()

    def leerTemperatura(self):
        return self.sensor.get_temperature()


archivo = open('temperatura_prom.txt','w')
suma = 0
contador = 0
sen = ib1820()
while True:
    tiempo_ahora = datetime.now()
    time_stamp = tiempo_ahora.timestamp()
    date_time = datetime.fromtimestamp(time_stamp)
    Temperatura = sen.leerTemperatura()
    str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")
    print("La temperatura es: %s°" %Temperatura)
    print("timestamp: ", str_date_time)
    contador += 1
    suma += Temperatura
    if(contador == 10):
        prom = str(suma/contador)
        suma = 0
        archivo.write("{} - {} \n".format(prom,str_date_time))


    time.sleep(30)
