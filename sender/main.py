import serial
import time

ser = serial.Serial('COM6', 115200)

while True:
    ser.write(b'[12:01:03] TEMP: 23.4 C\n')
    ser.write(b'[12:01:03] TEMP: 20.4 C\n')
    ser.write(b'[12:01:03] TEMP: 15.4 C\n')
    ser.write(b'[12:01:03] TEMP: 10.4 C\n')
    ser.write(b'[12:01:03] TEMP: 5.4 C\n')
    ser.write(b'[12:01:05] ERROR: Sensor disconnected\n')
    time.sleep(2)
