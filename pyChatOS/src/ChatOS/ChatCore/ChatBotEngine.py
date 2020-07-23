'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore.ChatBot import ChatBot 
import ChatOS.ChatIO as ChatIO
class ChatBotEngine(object):
    def __init__(self):
        self.currentChatBot=ChatBot('ChatDesktop')
        #self.currentChatBot.loadJson()
        #self.currentChatBot.model.train()
        #self.currentChatBot.model.save()
        self.currentIntent="None"
        self.output=ChatIO.output
        self.input =ChatIO.input
    def getInput(self):
        return self.input.getInput()
    def setOutput(self,response):
        self.output.setOutput(response)
    def run(self):
        while self.currentIntent!="goodbye":
            sentence=self.getInput()
            response,intent=self.currentChatBot.chat(sentence)
            self.currentIntent=intent
            self.setOutput(response)
        self.currentIntent="None"
