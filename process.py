import io
import os
import speech
import login
import json

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def halfp7(x, y):
  return (y >= x/2+7 and x >= y/2+7)

#iamge processing stuff
def imA(filepath, analysis, arg):
  try:
    client = vision.ImageAnnotatorClient()
    # The name of the image file to annotate
    file_name = os.path.join(
      os.path.dirname(__file__),
      filepath)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
      content = image_file.read()

    image = types.Image(content=content)
    if analysis == "labels":
    # Performs label detection on the image file
      response = client.label_detection(image=image)
      labels = response.label_annotations
      for label in labels:
        print(label.description)
    elif analysis == "facial":
      response = client.face_detection(image=image)
      facials = response.face_annotations
      open("include/facialjson.txt", 'w').close()
      facials = str(facials)
      with open("include/facialjson.txt", 'w') as text_file:
        text_file.write("{0}".format(facials))
      with open("include/facialjson.txt", 'r') as text_file:
        data = []
        bigdata = []
        for line in text_file:
          #print line
          if line.startswith("joy_likelihood:"):
            data.append(line.strip().lower())
            bigdata.append(line.strip().lower())
          elif "likelihood" in line:
            bigdata.append(line.strip().lower())
        for res in data:
          if "very_unlikely" in res or "unlikely" in res:
            speech.say("According to our image analysis, one or more of you is unhappy in this relationship.", arg)
            speech.say("Here are the full results:", arg)
            print data
            print " "
            print bigdata
            return 1
        speech.say("That's very cute, both of you seem happy in your relationship!", arg)
        speech.say("Here are the full results:", arg)
        print data
        print " "
        print bigdata
        return 1
    else:
      speech.say("Invalid image analysis request", arg)
  except:
    speech.say("Input Error",arg)
  
  return

#user input processing stuff
def processInput(i, s, userInfo, arg):
  if "logout" in i:
    speech.say("Okay, goodbye!", arg)
    return 0
  
  if "profile" in i or "account" in i:
    if "delete" in i:
      login.deleteProfile(s, arg)
      return 0
    elif "edit" in i:
      speech.say("Would you like to edit your password, gender, relationship status, or age?", arg)
      msg1 = speech.takeInput(arg)
      speech.say("What would you like it changed to?", arg)
      msg2 = speech.takeInput(arg)
      login.editProfile(s, userInfo, msg1, msg2, arg)
      return 1
    else:
      speech.say("Would you like to edit or delete your account?", arg)
      resp = speech.takeInput(arg)
      if "delete" in resp:
        login.deleteProfile(s, arg)
        return 0
      elif "edit" in resp:
        speech.say("Would you like to edit your password, gender, relationship status, or age?", arg)
        msg1 = speech.takeInput(arg)
        speech.say("What would you like it changed to?", arg)
        msg2 = speech.takeInput(arg)
        login.editProfile(s, userInfo, msg1, msg2, arg)
        return 1
      else:
        speech.say("Instruction not recognized", arg)
        return 1

  if "image analysis" in i:
    speech.say("I'd be happy to analyze an image for you, please type the filepath.", arg)
    fp = speech.takeInput(arg)
    speech.say("What type of image analysis would you like to do? Facial or Labels?", arg)
    analysis = speech.takeInput(arg)
    imA(fp, analysis, arg)
    return 1

  if "relationship" in i:
    if userInfo[2] != "single":
      #in a relationship
      speech.say("Would you like me to analyze your current relationship?", arg)
      r = speech.takeInput(arg)
      if "yes" in r:
        speech.say("Tell me about your significant other.", arg)
        speech.say("What is their gender?", arg)
        gr = speech.takeInput(arg)
        speech.say("What is their age?", arg)
        ga = speech.takeInput(arg) 
        if not halfp7(int(ga), int(userInfo[3])):
          speech.say("Your ages do not satisfy the half plus seven rule for dating.", arg)
          speech.say("This makes me deeply uncomfortable. I am deleting your profile", arg)
          login.deleteProfile(s, arg)
        else:
          speech.say("I would love to see how well you two get along.", arg)
          speech.say("Can you give me a picture of the two of you together?", arg)
          yn = speech.takeInput(arg)
          if "yes" in yn:
            speech.say("Okay, please type the filepath so I may perform image analysis.", arg)
            fp = speech.takeInput(arg)
            speech.say("In case you were curious, I found the following labels on your image.", arg)
            imA(fp, "labels", arg)
            imA(fp, "facial", arg)
            return 1
          else:
            speech.say("Okay, perhaps I can help you in another way.", arg)
            return 1
      else:
        speech.say("Okay, my mistake", arg)
        return 1
    else:
      speech.say("Single people are boring, go find a relationship!", arg)
      return 1
      #single person

  else:
    speech.say("Command not recognized", arg)
    return 1

