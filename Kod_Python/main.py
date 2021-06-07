#!/usr/bin/python3
from pocketsphinx import LiveSpeech
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import board
import adafruit_dht
import apa102

class VoiceAssistant:
    def __init__(self):
        self.lcd = LCD()
        self.dht = adafruit_dht.DHT22(board.D13, use_pulseio=False)
        self.leds = apa102.APA102(num_led=3, global_brightness=0b1)
        self.speech = LiveSpeech(
            kws = '/home/pi/voice-assistant-for-smart-buildings/Kod_Python/key.list',
            lm=False,
            verbose=True,
            sampling_rate=16000,
            buffer_size=1048,
            no_search=False,
            full_utt=False,
            )
        self.temp = 0
        self.humidity = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(12, GPIO.OUT)
        
    def __del__(self):
        GPIO.cleanup()

    def getSensorData(self):
        temp = 0
        humidity = 0
        try:
            temp = self.dht.temperature
            humidity = self.dht.humidity
        except RuntimeError as err:
            print(err.args[0])
        except Exception as err:
            self.dht.exit()
            raise err
        if(temp != None and humidity != None):
            self.temp = temp
            self.humidity = humidity

    def turnOnLed(self):
        GPIO.output(12, GPIO.HIGH)
    
    def turnOffLed(self):
        GPIO.output(12, GPIO.LOW)

    def turnOnRespeakerLeds(self, color = [72,61,139]):
        for x in range(3):
            self.leds.set_pixel(x, color[0], color[1], color[2])
            self.leds.show()

    def turnOffRespeakerLeds(self):
        self.leds.clear_strip()

    def viewTempOnLcd(self):
        self.lcd.clear()
        self.getSensorData()
        self.lcd.text("Temp: {:.1f} C".format(self.temp), 1)
        self.lcd.text("Humidity: {}% ".format(self.humidity), 2)
        # print("Temp: {:.1f} C Humidity: {}% ".format(self.temp, self.humidity))
    
    def action(self, words):
        tmp = str(words)
        if("show temperature" in tmp or "show humidity" in tmp):
            self.viewTempOnLcd()
            print("tu")
        if("lights on" in tmp):
            self.turnOnRespeakerLeds()
        if("lights off" in tmp):
            self.turnOffRespeakerLeds()
        if("lamp on" in tmp):
            self.turnOnLed()
        if("lamp off" in tmp):
            self.turnOffLed()
        if("set light color to red" in tmp):
            self.turnOnRespeakerLeds(color=[255,0,0])
        if("set light color to green" in tmp):
            self.turnOnRespeakerLeds(color=[0,255,0])
        if("set light color to blue" in tmp):
            self.turnOnRespeakerLeds(color=[0,0,255]) 

    def startRecognition(self):
        for phrase in self.speech:
            self.lcd.clear()
            print(phrase)
            self.lcd.text(str(phrase),1)
            self.action(phrase)
    
va = VoiceAssistant()
va.startRecognition()



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



