import telepot
from chatbot import Chatbot

telegram = telepot.Bot("")
bot = Chatbot("RedX")

def recebendoMsg(msg):
    frase = bot.escutar_bot(frase=msg['text'])
    resp = bot.pensa(frase)
    bot.fala(resp)

    tipoMsg, tipoChat, chatID = telepot.glance(msg)

    telegram.sendMessage(chatID, resp)

telegram.message_loop(recebendoMsg)

print('Módulo Telegram ativo! ok!')

while True:
    pass
