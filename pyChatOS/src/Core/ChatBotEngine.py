'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from Core.ChatBot import ChatBot 
from ChatIO.ChatOutputVoice import ChatOutputVoice
class ChatBotEngine(object):
    def __init__(self):
        self.currentChatBot=ChatBot('ChatDesktop')
        #self.currentChatBot.model.train()
        #self.currentChatBot.model.save()
        self.currentIntent="None"
        self.output=ChatOutputVoice()
    def getInput(self):
        return input('Ready: ')
    def setOutput(self,response):
        self.output.setOutput(response)
    def run(self):
        while self.currentIntent!="goodbye":
            sentence=self.getInput()
            response,intent=self.currentChatBot.chat(sentence)
            self.currentIntent=intent
            self.setOutput(response)
        self.currentIntent="None"