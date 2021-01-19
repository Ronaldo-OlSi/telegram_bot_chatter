import json
import sys
import os
import subprocess as s

class Chatbot():

    def __init__(self, nome):
        try:
            memoria = open(nome+'.json', 'r')
        except FileNotFoundError:
            memoria = open(nome+'.json', 'w')
            memoria.write('[["Joao", "Josi"], {"oi": "Olá, qual o seu nome?", "tchau!": "tchau!"}]')
            memoria.close()
            memoria = open(nome+'.json', 'r')
        self.nome = nome
        self.conhecidos, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None, ]

    def escutar_bot(self, frase=None):
        if frase is None:
            frase = input(">: ")
        frase = str(frase)
        if 'execut' in frase:
            return frase
        frase = frase.lower()
        frase = frase.replace("é", "eh")
        return frase

    def pensa(self, frase):
        if frase in self.frases:
            return self.frases[frase]
        if 'aprend' in frase:
            return 'Digite a dica: '

        ultimaFrase = self.historico[-1]
        if ultimaFrase == "Olá, qual o seu nome?":
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        if ultimaFrase == 'Digite a dica: ':
            self.chave = frase
            return 'Digite o significado da dica: '
        if ultimaFrase == 'Digite o significado da dica: ':
            resp = frase
            self.frases[self.chave] = resp
            self.gravaMemoria()
            return 'Aprendido! \u263a'
        try:
            resp = eval(frase)
            return str(resp)
        except:
            pass
        return "Não entendi... Ou não aprendi ainda..."

    def pegaNome(self, frase):
        if "o meu nome eh " in frase:
            nome = frase[14:].title()
        else:
            nome = frase
        return nome

    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = "Olá "
        else:
            frase = "Muito prazer "
            self.conhecidos.append(nome)
            self.gravaMemoria()
        return frase+nome

    def gravaMemoria(self):
        memoria = open(self.nome + '.json', 'w')
        json.dump([self.conhecidos, self.frases], memoria)
        memoria.close()

    def fala(self, frase):
        if 'executar' in frase:
            plataforma = sys.platform
            comando = frase.replace('executar ', '')
            if 'win' in plataforma:
                os.startfile(f'{comando}')
            if 'linux' in plataforma:
                try:
                    s.Popen(comando.lower())
                except FileNotFoundError:
                    s.Popen(['xdg-open', comando])
        else:
            print(frase)
        self.historico.append(frase)


