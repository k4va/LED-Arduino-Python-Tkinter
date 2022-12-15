import serial, time

arduino = serial.Serial("/dev/ttyACM0", 9600)

def encenderLED():
    arduino.write(b'1')
    time.sleep(1)

def apagarLED():
    arduino.write(b'0')
    time.sleep(1)