
import speech_recognition as sr

rec = sr.Recognizer()


with sr.Microphone() as fala:
   
    frase = rec.listen(fala)

print(rec.recognize_google(frase, language='pt'))
