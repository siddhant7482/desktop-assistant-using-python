import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kt
import smtplib
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#for speaking of the command
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
#basic wishing commands     
def wish(audio):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning Sir!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    
    else:
        speak("Good Evening sir !")
        
    speak("I am Hydra. Your Personal Assitant Please tell me how may I help you")

#take command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1 
        audio=r.listen(source)
    try:
        print("Recognizing.........")
        query = r.recognize_google(audio,language='en-in')
    except Exception as e : 
        print("Please repeat again...........")
        return "None"
    return query
#email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__": 
    wish("")
    while True:
     query = takecommand().lower()
     if 'wikipedia' in query:
        query = query.replace("wikipedia", "")
        speak("Searching wikipedia for ")
        speak(query)
        results = wikipedia.summary(query,sentences=4)
        speak("According to wikipedia")
        speak(results)
        print(results)
     elif 'open youtube' in query:
      speak("please tell the channel to be searched on youtube")
      a = takecommand()
      webbrowser.open_new_tab("https://www.youtube.com/"+ a)
     elif 'search' in query:
         speak("please tell the topic to be searched ")
         b = takecommand()
         kt.search(b)
     elif 'vs' in query:
         codePath = "C:\\Users\siddh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
         os.startfile(codePath)
     elif 'spyder' in query:
          codePath = "C:\\Users\siddh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Navigator (Anaconda3).lnk"
          os.startfile(codePath)
     elif 'game' in query:
          codePath = "C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk"
          os.startfile(codePath)
     elif 'android studio' in query:
          codePath = "C:\\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio\Android Studio.lnk"
          os.startfile(codePath)
     elif 'mail' in query:
           try:
               speak("to whom i should send the email")
               to = takecommand()
               speak("What should I say?")
               content = takecommand()
               sendEmail(to, content)
               speak("Email has been sent!")
           except Exception as e:
               print(e)
               speak("Sorry email failed") 
     elif 'message' in query:
         current_time = datetime.datetime.now() 
         speak("please mention the no. you want to send the message to ")
         number="+91"+takecommand()
         print(number)
         speak("please speak the message you want to send")
         message=takecommand()
         print(message)
         h=current_time.hour
         m=current_time.minute
         kt.sendwhatmsg(number, message, h, m)
        
    
          
    
   
        
       
         
      
    
        

        
    
    
