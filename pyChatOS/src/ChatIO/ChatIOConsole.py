'''
Created on 22 Jul 2020

@author: francisco
'''
from ChatIO import ChatIO

class ChatIOConsole(ChatIO):
    '''
    Traditional input from keyboard and output to screen in text mode
    '''
    def getInput(self):
        return input('Ready: ')
    def setOutput(self,response):
        print(response)