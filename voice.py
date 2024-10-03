import pyttsx3
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)