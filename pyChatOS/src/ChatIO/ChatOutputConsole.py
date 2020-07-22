'''
Created on 22 Jul 2020

@author: francisco
'''
from ChatIO.ChatOutput import ChatOutput

class ChatIOConsole(ChatOutput):
    '''
    Traditional output to screen in text mode
    '''
    def setOutput(self,response):
        print(response)