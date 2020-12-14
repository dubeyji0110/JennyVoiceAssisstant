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
        run_Jenny()
    return cmd

# function to execute the command
def run_Jenny():
    command = takeCmd()
    if 'play' in command:
        song = command[command.find('play')+4:]
        # song = command.replace('play', '')
        talk('Playing' + song + '...')
        pwk.playonyt(song)

    elif ('who are you' in command) or ('what are you' in command):
        talk("I'am Jenny, your personal Assisstant..!")

    elif ('tell me a joke' in command) or ('give me a joke' in command):
        talk(joke.get_joke())

    elif ('time' in command) and ('what' in command):
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current Time is: " + time)

    elif ('date' in command) and ('what' in command):
        date = datetime.date.today()
        talk(date)

    elif 'what' in command:
        search = command[command.find('what')+8:]
        # print(search)
        res = wiki.summary(search, 1)
        talk(res)

    elif 'who' in command:
        search = command[command.find('who')+7:]
        # print(search)
        res = wiki.summary(search, 1)
        talk(res)

    elif 'find' in command:
        search = command[command.find('find')+5:]
        # print(search)
        res = wiki.summary(search, 1)
        talk(res)

    elif ('power off' in command) or ('shutdown' in command) or ('shut down' in command):
        talk('Shutting Down..., Good Bye!')
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
