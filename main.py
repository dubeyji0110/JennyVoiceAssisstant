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
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(src)
            voice = listener.listen(src)
            cmd = listener.recognize_google(voice)
            if 'jenny' in cmd:
                cmd.replace('jenny', '')
            cmd = cmd.lower()
            print(cmd)
    except:
        # pass
        talk("Sorry, I can't understand!")
        # print('Listening...')
        # run_Jenny()
        return 0
    return cmd

# function to execute the command
def run_Jenny():
    command = takeCmd()
    if command == 0:
        return
    if 'play' in command:
        song = command[command.find('play')+4:]
        # song = command.replace('play', '')
        talk('Playing' + song + '...')
        pwk.playonyt(song)

    elif ('who are you' in command) or ('what are you' in command):
        talk("I'am Jenny, your personal Assisstant..!")

    elif ('tell me a joke' in command) or ('give me a joke' in command):
        talk(joke.get_joke())

    elif ('the time' in command):
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Current Time is: " + time)

    elif ('date' in command) and ('what' in command):
        date = datetime.date.today()
        talk(date)

    elif 'what' in command:
        search = command[command.find('what')+8:]
        # print(search)
        res = wiki.summary(search, 2)
        talk(res)

    elif 'who' in command:
        search = command[command.find('who')+7:]
        # print(search)
        res = wiki.summary(search, 2)
        talk(res)

    elif 'find' in command:
        search = command[command.find('find')+5:]
        # print(search)
        res = wiki.summary(search, 2)
        talk(res)

    elif ('power off' in command) or ('shutdown' in command) or ('shut down' in command):
        talk('Shutting Down..., Good Bye!')
        exit()

    else:
        talk("Sorry, I can't understand!")
        # print('Listening...')

# functoin for initial greeting
def greet():
    hrs = int(datetime.datetime.now().hour)
    if hrs < 4 and hrs >= 0:
        greeting = 'Good Night!,'
    if hrs >= 4 and hrs < 12:
        greeting = 'Good Morning!,'
    elif hrs >= 12 and hrs > 17:
        greeting = 'Good Afternoon!,'
    else:
        greeting = 'Good Evning!,'
    talk(greeting + " I'am Jenny your voice assistant!")
    talk("What can I do for you?")
    # print('Listening...')

if __name__ == "__main__":
    greet()
    while 1:
        print('Listining...')
        run_Jenny()
