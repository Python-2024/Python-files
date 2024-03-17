import pyttsx3

engine = pyttsx3.init()

audio1 = engine.say("Hello! I am your companion")
print(audio1)
engine.runAndWait()