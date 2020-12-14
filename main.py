import speech_recognition as sr
import pyttsx3 as t2s
import pywhatkit as pwk
import datetime
import wikipedia as wiki
import pyjokes as joke

listener = sr.Recognizer()
engine = t2s.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# function to play voice and print
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

# function to take(listen) command
def takeCmd():
    try:
        with sr.Microphone() as src:
            voice = listener.listen(src)
            cmd = listener.recognize_google(voice)
            if 'jenny' in cmd:
                cmd.replace('jenny', '')
            cmd = cmd.lower()
            print(cmd)
    except:
        # pass
        talk("Sorry, I can't understand!")
        print('Listening...')
        takeCmd()
    return cmd

# function to execute the command
def run_Jenny():
    cmd = takeCmd()
    if 'play' in cmd:
        song = cmd[cmd.find('play')+4:]
        # song = cmd.replace('play', '')
        talk('Playing' + song + '...')
        pwk.playonyt(song)

    elif ('who are you' in cmd) or ('what are you' in cmd):
        talk("I'am Jenny, your personal Assisstant..!")

    elif ('tell me a joke' in cmd) or ('give me a joke' in cmd):
        talk(joke.get_joke())

    elif ('time' in cmd) and ('what' in cmd):
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current Time is: " + time)

    elif ('date' in cmd) and ('what' in cmd):
        date = datetime.date.today()
        talk(date)

    elif 'what' in cmd:
        search = cmd[cmd.find('what')+8:]
        # print(search)
        res = wiki.summary(search, 1)
        talk(res)

    elif 'who' in cmd:
        search = cmd[cmd.find('who')+7:]
        # print(search)
        res = wiki.summary(search, 1)
        talk(res)

    elif 'find' in cmd:
        search = cmd[cmd.find('find')+5:]
        # print(search)
        res = wiki.summary(search, 1)
        talk(res)

    elif ('power off' in cmd) or ('shutdown' in cmd) or ('shut down' in cmd):
        talk('Good Bye!')
        exit()

    else:
        talk("Sorry, I can't understand!")
        # print('Listening...')

# functoin for initial greeting
def greet():
    talk("Greetings! I'am Jenny your personal assisstant!")
    talk("What can I do for you?")
    # print('Listening...')


greet()
while 1:
    print('Listining...')
    run_Jenny()
