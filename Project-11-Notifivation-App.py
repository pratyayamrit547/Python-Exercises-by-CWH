import plyer
import time as Time
import pyttsx3 as py
def notification(title,des,time):
    """THIS FUNCTION IS MAIN IN THIS CODE AS IT INITIALIZE ALL THE MODULES AND EXECUTE ALL ACTIONS PROPERLY"""
    #THIS IS NOW MAKING ARGUEMENT AS A VARIABLE
    headline=title
    description=des
    time=time
    speak=py.init()
    while True:
        #IN THIS BY THE USE OF PLYER WE ARE SENDING MESSAGE
        plyer.notification.notify(headline,description,timeout=10)
        #IN THIS BY USING PYTTSX3 WE ARE USING IT FOR PRONUCIATION OF DESCRIPTION OF NOTIFICATION
        speak.say(description)
        speak.runAndWait()
        #IN THIS USING TIME MODULE WE ARE USING SLEEP METHOD AND CONVERTING TIME INTO SECONDS
        Time.sleep(time)

def ask_the_user():
    """THIS FUNCTION IS MADE TO MAKE IT REUSABLE AND THIS FUNCTION TAKE TITLE, DES, TIME FROM USER FOR NOTIFICATION"""
    try:
        #TAKING INPUT FROM THE USER
        title=input("Give the Headline for the notification:")
        des=input("Give the Description for the notification:")
        ask_about_time=input("Do you want the time interval  between seconds{s}, minutes{m}, hours{h}:".lower())
        #If the user has chosen seconds than this if statement will work.
        if ask_about_time=="s":
            time_interval=input("Give the interval between seconds:")
            #this will check if the user has used any special character or not
            if time_interval.isnumeric():
                # PASSING IT TO NOTIFICATION FUNCTION AS A ARGUEMENT
                notification(title, des, time_interval)

            else:
                print("You have given inappropriate time")
        elif ask_about_time=="m":
            #If the user has chosen minutes than this elif statement will work.
            time_interval = input("Give the interval between minutes:")
            # this will check if the user has used any special character or not
            if time_interval.isnumeric():
                # PASSING IT TO NOTIFICATION FUNCTION AS A ARGUEMENT
                notification(title, des, int(time_interval)*60)
            # if user has used any special character than this else statement will work
            else:
                print("You have given inappropriate time")
        elif ask_about_time=="h":
            #if the user has chosen hour than this if statement will work
            time_interval = input("Give the interval between Hours:")
            # this will check if the user have used any special character or not
            if time_interval.isnumeric():
                # PASSING IT TO NOTIFICATION FUNCTION AS A ARGUEMENT
                notification(title, des, int(time_interval)*3600)
            # if user have used any special character than this else statement will work
            else:
                print("You have given inappropriate time")
        else:
            print("Give your choice only in {s},{m},{h}")
    except Exception as e:
        print(f"The problem occurred is this: {e}\nSorry for the inconvenience")


ask_the_user()
while True:
    try:
        ask=int(input("choose{1} for adding new notification choose{2} for exiting this:"))
        if ask==1:
            ask_the_user()
        elif ask==2:
            print("You have successfully exited the notification app")
        else:
            print("GIVE ONLY 1 AND 2 AS YOUR CHOICE".title())
    except Exception as e:
        print(f"The problem occurred is this: {e}\nSorry for the inconvenience")
