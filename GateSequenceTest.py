import time as t
import smbus
import simpleaudio as sa


DEVICE_BUS = 1
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)


okRiders = sa.WaveObject.from_wave_file('OkRidersRandomStart.wav')
ridersReady = sa.WaveObject.from_wave_file('RidersReadyWatchTheGate.wav')
shortTone = sa.WaveObject.from_wave_file('632_60ms.wav')
longTone = sa.WaveObject.from_wave_file('632_2250ms.wav')

def playAudioBlocking( wave ):
    play_obj = wave.play()
    play_obj.wait_done()

def turnOnRelay( relayNumber ):
    bus.write_byte_data(DEVICE_ADDR, relayNumber, 0xFF)
    
def turnOffRelay( relayNumber ):
    bus.write_byte_data(DEVICE_ADDR, relayNumber, 0x00)

while True:
    
    playAudioBlocking(okRiders)
    t.sleep(1.8)
    
    playAudioBlocking(ridersReady)
    t.sleep(1.5)
    
    try:
        for i in range(1,4):
            turnOnRelay(i)
            playAudioBlocking(shortTone)
            t.sleep(0.060)
            
        turnOnRelay(4)
        playAudioBlocking(longTone)
        
        for i in range(1,5):
            turnOffRelay(i)
        t.sleep(5.00)    
        
    except KeyboardInterrupt as e:
        print("Quit the Loop")
        exit()
        

