'''
Created on 28 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.Chatgets.ChatField import ChatField
import ChatOS.ChatIO as ChatIO
from ChatOS.ChatCore.ChatExceptions import ChatExceptionMisunderstand, ChatExceptionScape

class CreateChatBot(ChatField):
    def __init__(self, chatBot):
        super().__init__(chatBot)
        self.output=ChatIO.output
    def exec(self,sentence=""):
        ccb=self.chatBot.getCurrentChatBot()
        if ccb!=None:
            #ask wheter save or discard the current chat bot
            pass
        try:
            #ask for name of the chatbot
            self.output.setOutput('Could you please tell me the name of the chatbot you want to create?')
            newSentence=super().exec(sentence)
            ccb.createChatBot(newSentence)
            self.output.setOutput("The chatbot named "+newSentence+" has been created.")
        except ChatExceptionScape as ces:
            return
        except ChatExceptionMisunderstand as cem:
            return
        
         