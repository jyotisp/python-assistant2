import pyttsx3

import os

while True:

    pyttsx3.speak("Chat with me for your requirements")
    p=input("Enter your requirement")
 
    if(("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("text editor" in p)):
      print("which text editor you want? notepad or notepad++")
      p1=input()
      if(p1=="notepad"):
        os.system("notepad")
      elif(p1=="notepad++"):
        os.system("notepad++")
      else:
        print("dont support")
 
    elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("candy crush" in p) or ("game" in p)):
      os.system("Candy Crush Saga")

    elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("docuents" in p) or ("docs" in p)):
      os.system(os.startfile("Documents"))

    elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("camera" in p)):
      os.system("camera")
    
    elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("powerpoint" in p)):
      os.system("powerpoint")

    elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("microsoft edge" in p) or ("microsoft edge" in p)):
      os.system("microsoft edge")

    elif(("run" in p) or ("execute" in p) or ("open" in p)) and (("photos" in p) or ("pics" in p)):
      os.system(os.startfile("F:/photos"))

    elif(("run" in p) or ("execute" in p) or ("open" in p)) and ("youtube" in p):
      os.system("microsoft edge/youtube.com")

    elif("exit" in p) or ("quit" in p):
      break;

    

    else:
      print("dont support")
