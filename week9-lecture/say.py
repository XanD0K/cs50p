import cowsay
import pyttsx3 # Python's text to speech library

engine = pyttsx3.init()
this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
