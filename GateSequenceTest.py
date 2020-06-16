import time as t
import smbus
import simpleaudio as sa


DEVICE_BUS = 1
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)


okRiders = sa.WaveObject.from_wave_file('OkRidersRandomStart.wav')
ridersReady = sa.WaveObject.from_wave_file('RidersReadyWatchTheGate.wav')

wave_short = sa.WaveObject.from_wave_file('632_60ms.wav')
wave_long = sa.WaveObject.from_wave_file('632_2250ms.wav')


def turnOnRelay( relayNumber ):
    bus.write_byte_data(DEVICE_ADDR, relayNumber, 0xFF)
    
def turnOffRelay( relayNumber ):
    bus.write_byte_data(DEVICE_ADDR, relayNumber, 0x00)

while True:
    
    play_obj = okRiders.play()
    play_obj.wait_done()
    
    t.sleep(1.8)
    
    play_obj = ridersReady.play()
    play_obj.wait_done()
    
    t.sleep(1.5)
    
    try:
        for i in range(1,4):
            turnOnRelay(i)
            play_obj = wave_short.play()
            play_obj.wait_done()
            t.sleep(0.060)
            
        turnOnRelay(4)
        play_obj = wave_long.play()
        play_obj.wait_done()
        for i in range(1,5):
            turnOffRelay(i)
        t.sleep(5.00)    
        
    except KeyboardInterrupt as e:
        print("Quit the Loop")
        exit()
        

