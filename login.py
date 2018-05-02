import speech

import getpass

def lower(lst):
  lst = [l.lower() for l in lst]
  return lst

def strip(lst):
  lst = [l.strip() for l in lst]
  return lst

def createProfile(s, arg):
  speech.say("Hi " + s + ", let's set up your profile", arg)
  speech.say("What would you like your password to be?", arg)
  newpass = getpass.getpass('Password: ').lower()
  speech.say("What is your gender?", arg)
  gender = speech.takeInput(arg)
  speech.say("What is your relationship status?", arg)
  rs = speech.takeInput(arg)
  speech.say("What is your age?", arg)
  age = speech.takeInput(arg)
  with open("include/profiles.txt",'a') as newf:
    newf.write(s+","+newpass+","+gender+","+rs+","+age+"\n")
  speech.say("Your account has been stored!", arg)
  return [s,[newpass,gender,rs,age]]

#Login
def loginAttempt(s, arg):
  s = s.lower()
  with open("include/profiles.txt") as f:
    content = f.readlines()
  users = {profile.split(",")[0].lower() : strip(lower(profile.split(",")[1:])) for profile in content}
  
  if s in users.keys():
    speech.say("Name recognized", arg)
    speech.say("Hi " + s + ", for security, type your password", arg)
    return [getpass.getpass('Password: ').lower() == users[s][0], users[s]]
  else:
    speech.say("Name not recognized", arg)
    return [0, ""]

def editProfile(s, userInfo, msg1, msg2, arg):
  if "password" in msg1:
    userInfo[0] = msg2
  elif "gender" in msg1:
    userInfo[1] = msg2
  elif "relationship status" in msg1:
    userInfo[2] = msg2
  elif "age" in msg1:
    userInfo[3] = msg2
  else:
    speech.say("Invalid request", arg)
    return 1
  internalDeleteProfile(s, arg)
  with open("include/profiles.txt",'a') as newf:
    newf.write(s+","+userInfo[0]+","+userInfo[1]+","+userInfo[2]+","+userInfo[3]+"\n")
  speech.say("Edit complete", arg)
  return 1

def deleteProfile(s, arg):
  with open("include/profiles.txt", "r") as f2:
    content = f2.readlines()
  f2.close()
  with open("include/profiles.txt", "w") as f2:
    for line in content:
      if not s.strip().lower() in strip(lower(line.split(","))):
        f2.write(line)
  speech.say("Profile deleted, logging you out now!", arg)

def internalDeleteProfile(s, arg):
  with open("include/profiles.txt", "r") as f2:
    content = f2.readlines()
  f2.close()
  with open("include/profiles.txt", "w") as f2:
    for line in content:
      if not s.strip().lower() in strip(lower(line.split(","))):
        f2.write(line)
