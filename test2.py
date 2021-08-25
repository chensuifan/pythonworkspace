import serial
import serial.tools.list_ports

var=serial.tools.list_ports.comports()

print("%s" %var)  