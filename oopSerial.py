import serial

class temperatura():
    def __init__(self):
        self.sensor = serial.Serial('/dev/ttyACM0',9600)

    def leer_sensor(self):
        lineBytes = self.sensor.readline()
        line = lineBytes.decode('utf-8').strip()
        return(line)


sensor = temperatura()

while True:
    line = sensor.leer_sensor()
    line = str(line)
    print(line)
