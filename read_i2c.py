

import smbus
import time

bus = smbus.SMBus(1)

addres = 0x04

while True:
        text  = bytes(bus.read_i2c_block_data(addres, 0, 9)).decode("ascii") 
        print (text)
        print()

