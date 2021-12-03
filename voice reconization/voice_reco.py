# try :
#      import speech_recognition as sr
#      import datetime
#      import pyttsx3
# except Exception as e :
#      print(f"Somethig is wrong with importing {e}")


# # import sys
# # import pydub


# engine = pyttsx3.init('sapi5')

# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0])

# def speak(audio):
#      ''' This is a function which help to Speek the things '''
#      engine.say(audio)
#      engine.runAndWait()


# def wishme():
#      '''
#      This is a Function which wish me on start
#      '''
#      hour = int(datetime.datetime.now().hour)
#      if hour >=0 and hour < 12:
#           speak("Good Moring !")

#      elif hour>=12 and hour<17:
#           speak("Good Afternoon Sir !")

#      else:
#           speak("Good evening")

#      speak("\nI'm Jarvis \n How Can i HElp you")

# # wishme()

# def takeCommand():
#      '''It takes microphone voice as input recognise it..'''
#      r = sr.Recognizer()
#      with sr.Microphone() as source:
#           print("listing")
#           r.pause_threshold = 1
#           audio = r.listen(source)
#      try: 
#           print("Recoginiting...")
#           query = r.recognize_google(audio, language = 'en-in') 
#           print(f"User said {query}")

#      except Exception as e:
#           print(e)     
#           print("Say that again please ...")
#           return "Nono"
#      return query     

# print(takeCommand())


# import urllib.request as ur
# from urllib.request import Request, urlopen
# import os


src = 'https://irctclive.nlpcaptcha.in/index.php/media/voicecaptcha/akZlNjVxOGZJRjVlWkFkWTZSOFhoY3lPNVVyU2l5SWdCamZaNzN5MVpreXpqK1UxOFFDODl2T25sYUVYdFZhbGhkQ21PRmplZXZDS09lVVVnUWZmWHc9PQ==/wav' 


import urllib.request
urllib.request.urlretrieve(src, "src.mp3")

# path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
# path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))
# req = Request(src)
# urlopen(req).read()

# ur.urlretrieve(src, path_to_mp3)
