'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore import ChatBot
class MetaChatBot(ChatBot):
    '''
    A chatbot to build and modify chatbots
    '''
    def __init__(self):
        '''
        Constructor
        '''
        super('MetaChatBot')
        self.currentChatBot=None
        self.currentIntent=None
    def createChatBot(self,name):
        self.currentChatBot=ChatBot(name)
    def addIntent(self,name):
        intent=Intent(self.currentChatBot,name)
        self.currentChatBot.addIntent(intent)
        self.currentIntent=intent
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