from chatbot import Chatbot
import pyttsx3
import speech_recognition as sr

en = pyttsx3.init()
en.setProperty('voice', 'brazil+f1')
rec = sr.Recognizer()

class BotFalante(Chatbot):

    def escuta(self, frase=None):
        try:
            with sr.Microphone() as mic:
                fala = rec.listen(mic)
            frase = rec.recognize_google(fala, language='pt')
            print(frase)
        except sr.UnknownValueError:
            print('Erro ao identificar a voz...')
            return ''

        return super().escutar_bot(frase=frase)

    def fala(self, frase):
        en.say(frase)
        en.runAndWait()
        super().fala(frase)

Bot = BotFalante('Felipe')

while True:

    frase = Bot.escuta()
    resp = Bot.pensa(frase)
    Bot.fala(resp)

    if resp == "tchau!":
        break