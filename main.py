from pickle import TRUE
import pyaudio
import speech_recognition as sr
import pyjokes
import wikipedia
import datetime
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def talk(text):
    engine.say(text)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    try:
        with sr.Microphone() as source:
            print('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # command =input('enter the command ')
            if 'alexa ' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    #command = takecommand()
    command = 'play ganja burn'
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M')
        print(time)
        talk('current time is ' + time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again ')


while True:
    run_alexa()

