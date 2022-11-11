import pywhatkit as kit
import pyttsx3
playnow = input(str("Enter what do u want me to play?  :     "))
kit.playonyt(playnow)

plus_sign = '+'
cc = '91'

engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

engine.say("What is the recipient's phone number, sir?, type here")
engine.runAndWait()
print("What is the recipient's phone number, sir? Type here")
input_ph_no= int(input("Type Ph. Number here:   "))
contostring=str(input_ph_no)

ph_with_code= plus_sign + cc + contostring
print("target: ", ph_with_code)


engine.say("Okay, now What is the message you want to convey, sir?, type here")
engine.runAndWait()
print("What is the message you want to convey, sir? Type here")
input_msg= str(input("Type Here:  "))

engine.say("Okay, now at which hour the message should be delivered, sir?, type here")
engine.runAndWait()
print("At Which hour the message should be delivered, sir? Type here")

input_hour= int(input("Type Here:  "))

engine.say("And at what minute?, type here")
engine.runAndWait()
print("At what minute, sir? Type here")
input_minute= int(input("Type Here:  "))


kit.sendwhatmsg(ph_with_code, input_msg, input_hour, input_minute)
