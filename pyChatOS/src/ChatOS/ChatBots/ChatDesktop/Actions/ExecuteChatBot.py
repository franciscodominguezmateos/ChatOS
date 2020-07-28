'''
Created on 27 Jul 2020

@author: Francisco Dominguez
'''
import ChatOS
from ChatOS.Chatgets.ChatField import ChatField
from ChatOS.ChatCore.ChatExceptions import ChatExceptionMisunderstand, ChatExceptionScape

class ExecuteChatBot(ChatField):
    def __init__(self, chatBot):
        '''
        Constructor
        '''
        super().__init__(chatBot)
    def exec(self,sentence):
        try:
            newSentence=super().exec(sentence)
            ChatOS.chatBotEngine.launchChatBot(newSentence)
        except ChatExceptionScape as ces:
            return
        except ChatExceptionMisunderstand as cem:
            return
        
        