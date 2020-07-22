'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from Core import ChatBot
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
    