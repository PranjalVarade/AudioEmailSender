import smtplib  #simple Mail Transfer Protocol
import speech_recognition as speechr
import pyttsx3
from email.message import EmailMessage
listen = speechr.Recognizer()
engine = pyttsx3.init()


email_book = {
    'abc': 'abc@gmail.com',
    'xyz': 'xyz@gmail.com'
}
'''In the email list put the receivers name and there email address'''

def speak(text):
    engine.say(text)
    engine.runAndWait()


def audio_input():
    try:
        with speechr.Microphone() as input_val:
            print("I am listening")
            voice = listen.listen(input_val)
            information = listen.recognize_google(voice)  #converts the audio into text
            print(information)
            return information.lower()
    except:
        pass


def send_auto_email(receiver, sub, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)  #server
    server.starttls()  #tls= Transport Layer Securiy
    server.login('prtestmail@gmail.com', 'pr')
    '''In server.login give details of senders email address and password '''
    '''Also you will need to change the setting with gmail account given in READ ME file '''
    email = EmailMessage()
    email['From'] = 'pranjalsvtestmail@gmail.com'
    email['To'] = receiver
    email['Subject'] = sub
    email.set_content(msg)
    server.send_message(email)



def get_info_email():
    speak('Receiver of the email')
    name = audio_input()
    receiver = email_book[name]
    #print(receiver)
    speak('subject of your email')
    sub = audio_input()
    speak('message you want to send')
    msg = audio_input()

    send_auto_email(receiver, sub, msg)
    speak("hey your email send")
    speak(" do want to send more email?")
    ans = audio_input()
    if ans == 'yes':
        get_info_email()
    elif ans == 'no':
        speak('ok bye bye ')


get_info_email()
