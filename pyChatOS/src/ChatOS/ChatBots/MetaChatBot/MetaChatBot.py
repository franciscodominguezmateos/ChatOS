'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore import ChatBot
from ChatOS.ChatCore import Intent

class MetaChatBot(ChatBot):
    '''
    A chatbot to build and modify chatbots
    '''
    def __init__(self):
        super('MetaChatBot')
        self.currentChatBot=None
        self.currentIntent=None
    def getCurrentChatBot(self): return self.currentChatBot
    def getCurrentIntent(self):  return self.currentIntent
    def createChatBot(self,name):
        self.currentChatBot=ChatBot(name)
    def addIntent(self,name):
        intent=Intent(self.currentChatBot,name)
        self.currentChatBot.addIntent(intent)
        self.currentIntent=intent
    def addPattern(self,pattern):
        self.currentIntent.addPatern(pattern)
    def addResponse(self,s):
        self.currentIntent.addResponse(s)
'''
- create chatbot
- add intent
- add patterns
- add responses
- add action
- create skeleton for actions
- run chatbot
- load chatbot
- save chatbot
- 
'''    