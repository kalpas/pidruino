import serial

port=  serial.Serial('/dev/ttyUSB0', 9600)
port.readline();
while 1:
	if(port.in_waiting > 0):
		line = str(port.readline().decode().strip('\r\n'))
		print(line)
