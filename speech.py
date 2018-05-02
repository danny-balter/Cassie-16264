#import speech_recognition as sr
#import pyttsx

#Speech Stuff
#engine = pyttsx.init()
#r = sr.Recognizer()

def say(s, arg):
  if arg == "chat":
    print s
    return
  elif arg == "voice":
    #engine.say(s)
    #a = engine.runAndWait()
    return
  else:
    print "invalid arg"
    return

#Command Functionality
def takeInput(arg):
#returns processed string
  if arg == "chat":
    s = raw_input("> ").lower()
    return s
  elif arg == "voice":
    return
    #with sr.Microphone() as source:
    #  audio = r.listen(source)
    #  try:
    #    s = r.recognize_google(audio)
    #    return s
    #  except:
    #    say("Speak more clearly.")
    #    takeInput(arg)
  else:
    print "invalid arg"
    return