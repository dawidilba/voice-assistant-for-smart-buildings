import apa102
import pyaudio 
import wave
import os

RATE = 16000 # max sample rate of respeaker is 48kHz, for speech recognition 16kHz is sufficient
CHANNELS = 2 # stereo
BITS_WIDTH = 2 # sample bits width 
CHUNK = 1024
REASPEAKER_ID = 0

leds = apa102.APA102(num_led=3, global_brightness=0b1)

def ledsTurnOn():
    color = [72,61,139]
    for x in range(3):
        leds.set_pixel(x, color[0], color[1], color[2])
        leds.show()

def ledsTurnOff():
    leds.clear_strip()

def record(time):
    pyAudio = pyaudio.PyAudio()
    stream = pyAudio.open(rate=RATE, format=pyAudio.get_format_from_width(BITS_WIDTH), channels=CHANNELS, input=True, input_device_index=REASPEAKER_ID)
    data = []
    ledsTurnOn()
    for i in range(0, int(RATE/CHUNK * time)):
        val = stream.read(CHUNK)
        data.append(val)
    ledsTurnOff()
    stream.stop_stream()
    stream.close()
    pyAudio.terminate()
    return data

def save(fileName, time):
    w = wave.open(fileName + ".wav", 'wb')
    w.setframerate(RATE)
    w.setnchannels(CHANNELS)
    w.setsampwidth(BITS_WIDTH)
    w.writeframes(b''.join(record(time)))
    w.close()

save("output", 3)
os.system("aplay -Dhw:2,0 output.wav")
