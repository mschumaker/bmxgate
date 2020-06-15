import time as t
import smbus

DEVICE_BUS = 1
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)

def turnOnRelay( relayNumber ):
    bus.write_byte_data(DEVICE_ADDR, i, 0xFF)
    
def turnOffRelay( relayNumber ):
    bus.write_byte_data(DEVICE_ADDR, i, 0x00)

while True:
    try:
        for i in range(1,5):
            turnOnRelay(i)
            t.sleep(0.120)
        t.sleep(2)
        for i in range(1,5):
            turnOffRelay(i)
        
    except KeyboardInterrupt as e:
        print("Quit the Loop")
        exit()
        

