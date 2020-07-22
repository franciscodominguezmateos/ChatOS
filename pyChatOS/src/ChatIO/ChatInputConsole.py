'''
Created on 22 Jul 2020

@author: francisco
'''
from ChatIO import ChatInput

class ChatInputConsole(ChatInput):
    '''
    Traditional input from keyboard and output to screen in text mode
    '''
    def getInput(self):
        return input('Ready: ')