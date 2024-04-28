import time # time module
import pyttsx3 # text to speech module
def Test_to_speech():
    pass


def Good_morning():
    sound.say(f"Good Morning {name} ")
    sound.say("now the time is" + time.strftime("%H hours  %M minutes and %S seconds"))
def Good_afternoon():
    sound.say(f"Good Afternoon {name} ")
    sound.say("now the time is" + time.strftime("%H hours  %M minutes and %S seconds"))
def Good_evening():
    sound.say(f"Good Evening {name} ")
    sound.say("now the time is" + time.strftime("%H hours  %M minutes and %S seconds"))
def Good_night():
    sound.say(f"Good Night {name} ")
    sound.say("now the time is" + time.strftime("%H hours  %M minutes and %S seconds"))
while True:
    try:
        name = input("Give your name:")
        sound = pyttsx3.init()# it is the main engine or start button for the text to speech
        hour = time.strftime("%H") #time.strftime tell us real time year,month,day as well as hour,minutes and seconds
        int_hour = int(hour)
        print(hour)
        if int_hour >= 21:
                Good_night()
        elif int_hour == 4 or (int_hour < 12):
            Good_morning()
        elif int_hour == 12 or int_hour < 16:
            Good_afternoon()
        elif int_hour == 16 or (int_hour < 21):
            Good_evening()
        sound.runAndWait()# It executes the text to speech
        break
    except:
        print("Sorry for the inconvenience.\nPlease try again one more time")
