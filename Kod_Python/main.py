#!/usr/bin/python3
from pocketsphinx import LiveSpeech
from rpi_lcd import LCD
import board
import adafruit_dht

lcd = LCD()
dhtDevice = adafruit_dht.DHT22(board.D13)

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
)

def viewSensorInfoOnLCD():
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
    except:
        temperature_c = 0
        humidity = 0

    lcd.text("Temp: {:.1f} C".format(temperature_c), 1)
    lcd.text("Humidity: {}% ".format(humidity), 2)


for phrase in speech:
    print(phrase)
    if(phrase == "temperature"):
        viewSensorInfoOnLCD()
    else:
        lcd.clear()
        


# import wave
# import os
# import pyaudio 
# from speech_recognition import Microphone, Recognizer, AudioFile
# import speech_recognition as sr

# # mic = Microphone()

# # for i in mic.list_microphone_names():
# #     print(i)

# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.record(source, 3)
# print("stop")

# print(r.recognize_google(audio))
# recognize speech using Sphinx
# try:
#     print(r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))



