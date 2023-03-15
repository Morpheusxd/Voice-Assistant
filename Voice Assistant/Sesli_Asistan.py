from gtts import gTTS 
from playsound import playsound
import speech_recognition as sr
import random
import os
import pyfiglet
import webbrowser 
import time
import pyautogui
from termcolor import colored
import subprocess



r = sr.Recognizer()

def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        try:
            voice = r.recognize_google(audio, language='tr-TR', show_all=True)
            voice_json = voice['alternative'][0]
            transcript = voice_json['transcript']
            # Küçük harfe dönüştür
            transcript = transcript.lower()
            return transcript
        except sr.UnknownValueError:
            speak('Anlayamadım, tekrar deneyin.')
        except sr.RequestError:
            speak("ne dedin, anlamadım , acaba tekrar edermisin")
        except IndexError:
            speak('Anlayamadım, tekrar deneyin.')
        except TypeError:
            speak("ne dedin anlayamadım , acaba tekrar edermisin")

def listen():
    while True:
        voice = record()
        print(terminal1, voice)
        yanit(voice)    
        
terminal1 = """
┌──(root💀Admin)-[~]
└─#"""
terminal2 = """
┌──(user㉿user)-[~]
└─$"""


def get_credentials():
    speak('Lütfen kullanıcı adınızı söyleyin.')
    username = record()
    print(terminal1, username)
    speak('Şimdi de parolanızı söyleyin.')
    password = record()
    print(terminal1, password)
    return username, password

def authenticate():
    username, password = get_credentials()
    if username == 'admin' and password == 'admin':
        speak('Giriş başarılı. Hoş geldiniz.')
        text = pyfiglet.figlet_format("Admin")
        os.system("cls")
        os.system("color a")
        text = pyfiglet.figlet_format("Voice Assistant")
        print(text)
        # input_str = "Hoşgeldin Admin"
        # for c in input_str:
        #     if c == ' ':
        #         colored_char = ' '
        #     else:
        #         if ord(c) % 2 == 0:
        #             colored_char = colored(c, color='green')
        #         else:
        #             colored_char = colored(c, color='red')
        #     print(colored_char, end='')
    else:
        speak('Kullanıcı adı veya parola yanlış. Tekrar deneyin.')
        return authenticate()
    
    
def speak(string):
    if string:
        tts = gTTS(string, lang='tr')
        rand = random.randint(1, 10000)
        file = 'audio-' + str(rand) + '.mp3'
        tts.save(file)
        playsound(file)
        os.remove(file)

speak('Sisteme hoş geldiniz.')
authenticate()


def yanit(voice):
    if voice is None:
        return
    if "ben kimim" in voice:    
        speak("Admin")
        
    if "yetkilerim neler" in voice:
        speak("Yetkilerin Sınırsız Admin")
        
    if "merhaba" in voice and voice == "merhaba" :
        speak("Sanada Merhaba Dostum")
        
    if "çıkış yap" in voice and voice == "çıkış yap":
        speak("Çıkış yapılıyor")
        quit()
        
    if "teşekkür ederim" in voice and voice == "teşekkür ederim":
        speak("ben teşekkür ederim admin")
        
    if "matrix başlat" in voice and voice == "matrix başlat":
        pyautogui.press("f11")
        process = subprocess.Popen(["matrix-rain"])
        time.sleep(10)
        pyautogui.press("f11")
        process.terminate()
        os.system("cls")
    if "ekranı temizle" in voice and voice == "ekranı temizle":
        os.system("cls")   
    
    if "terminali kırmızı yap" in voice and voice == "terminali kırmızı yap":
        os.system("color 4")
    if "terminali beyaz yap" in voice and voice == "terminali beyaz yap":
        os.system("color 7")
    if "terminali mavi yap" in voice and voice == "terminali mavi yap":
        os.system("color 1")
    if "terminali yeşil yap" in voice and voice == "terminali yeşil yap":
        os.system("color a")
    if "terminali pembe yap" in voice and voice == "terminali pembe yap":
        os.system("color 5")
    
    
    if "youtube arama yap" in voice and voice == "youtube arama yap":
        search_youtube = record('ne aramamı istersin') 
        urly ='https://www.youtube.com/results?search_query='+search_youtube
        webbrowser.get().open(urly)
        speak(search_youtube+' için bulduğum sonuçlar')
        print("Admin = "+search_youtube+' için bulduğum sonuçlar')
    
    if "google arama yap" in voice and voice == "google arama yap":
        search = record('ne aramamı istersin')
        url ='https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search+' için bulduğum sonuçlar')
        print("Admin  = "+search+' için bulduğum sonuçlar')

      
             
while True:
    voice = record()
    speak(voice)
    print(terminal1, voice)
    yanit(voice)
    
# coded by Morpheus
