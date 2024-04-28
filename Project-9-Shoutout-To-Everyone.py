import pyttsx3
sound = pyttsx3.init() # it is the main engine or start button for the text to speech
list = ["rohan" , "sohan" , "hemant" , "prasad"]
for i in list:
    sound.say("Shoutout to "+i) # it is the function which says our text
sound.runAndWait()# It executes the text to speech
