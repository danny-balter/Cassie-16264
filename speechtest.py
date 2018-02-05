import speech_recognition as sr
import pyttsx
import datetime

r = sr.Recognizer()
with sr.Microphone() as source:
  print("Hi, I'm Cassie, what would you like me to do?")
  audio = r.listen(source)

engine = pyttsx.init()

harmKeywords = ["kill myself", "hurt myself", "harm myself"]
journal = {}

try:
  s = r.recognize_google(audio)
  for word in harmKeywords:
    if word in s:
      print "Self Harm Keyword Detected"
      engine.say("You are threatening self harm, connecting you to 9 1 1")
      engine.runAndWait()
      break
  if "journal" in s:
    engine.say("accessing journal")
    engine.runAndWait()
    journal()
  else:
    engine.say("You said: " + audio + " which was an unrecognized command")

except sr.UnknownValueError:
  print("Could not understand audio")

except sr.RequestError as e:
  print("Could not request results; {0}".format(e))

def create_new_journal_entry():
  time = datetime.datetime.now()
  journal[time] = ""
  engine.say("Journal began:")
  with sr.Microphone() as source:
    audio = r.listen(source)
  try:
    s = r.recognize_google(audio)
  except:
    engine.say("I did not understand that")
    engine.runAndWait()
  journal[time] = s

def journal():
  engine.say("would you like to access an old entry or read a new one?")
  engine.runAndWait()
  with sr.Microphone() as source:  
    audio = r.listen(source)
  try:
    s = r.recognize_google(audio)
    if "new" in s:
      create_new_journal_entry()
  except:
    engine.say("I did not understand that")
    engine.runAndWait()
  return
