import speech
import login
import process

import sys
import datetime

#######################################################
#######################################################

def main(arg):
  speech.say("Hi, I'm Cassie, who are you?", arg)
  s = speech.takeInput(arg)
  result = login.loginAttempt(s, arg)
  while not result[0]:
    speech.say("Login failed, would you like to make an account?", arg)
    resp = speech.takeInput(arg)
    if "yes" in resp:
      result = login.createProfile(s, arg)
      speech.say("You've been logged in!", arg)
      break
    else:
      speech.say("Would you like to try logging in again?", arg)
      resp2 = speech.takeInput(arg)
      if "yes" in resp2:
        result = login.loginAttempt(s, arg)
      else:
        speech.say("Okay, goodbye!", arg)
        return
  
  speech.say("Welcome back " + s, arg)

  cont = 1
  #password, gender, relationship status, age
  userInfo = result[1]
  while(cont):
    speech.say("How can I help you?", arg)
    cont = process.processInput(speech.takeInput(arg), s, userInfo, arg)

  return

#######################################################
#######################################################

#Running Cassie
arg = sys.argv[1]
main(arg)