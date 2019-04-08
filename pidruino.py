import smbus
import time

bus = smbus.SMBus(1)

addres = 0x04

def writeNumber(value):
        bus.write_byte(addres, value)
        return -1

def readNumber():
        number = bus.read_byte(addres)
        return number

while True:
        var = eval(input("Enter 1 - 9: "))
        if not var:
                continue

        writeNumber(var)
        print ("sent: ", var)
        time.sleep(1)

        number  =  readNumber()
        print ("got: ", number)
        print()

