'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
class ChatBotEngine(object):
    def __init__(self):
        self.currentChatBot=ChatBot('intents')
        self.currentIntent="None"
    def getInput(self):
        return input('Ready: ')
    def setOutput(self,response):
        print(response)
    def run(self):
        while self.currentIntent!="goodbye":
            sentence=self.getInput()
            response,intent=self.currentChatBot.chat(sentence)
            self.currentIntent=intent
            self.setOutput(response)
        self.currentIntent="None"