from pocketsphinx import LiveSpeech

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
)
for phrase in speech:
    print(phrase)


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


# RATE = 16000 # max sample rate of respeaker is 48kHz, for speech recognition 16kHz is sufficient
# CHANNELS = 2 # streo
# BITS_WIDTH = 2 # sample bits width 
# CHUNK = 1024
# REASPEAKER_ID = 0


# def record(time):
#     pyAudio = pyaudio.PyAudio()
#     stream = pyAudio.open(rate=RATE, format=pyAudio.get_format_from_width(BITS_WIDTH), channels=CHANNELS, input=True, input_device_index=REASPEAKER_ID)
#     data = []
#     for i in range(0, int(RATE/CHUNK * time)):
#         ledsTurnOn(i)
#         ledsTurnOnEnd(i)
#         val = stream.read(CHUNK)
#         data.append(val)
#     stream.stop_stream()
#     stream.close()
#     pyAudio.terminate()
#     return data

# def save(fileName, time):
#     w = wave.open(fileName + ".wav", 'wb')
#     w.setframerate(RATE)
#     w.setnchannels(CHANNELS)
#     w.setsampwidth(BITS_WIDTH)
#     w.writeframes(b''.join(record(time)))
#     w.close()

# save("output", 3)
# os.system("aplay -Dhw:2,0 output.wav")
