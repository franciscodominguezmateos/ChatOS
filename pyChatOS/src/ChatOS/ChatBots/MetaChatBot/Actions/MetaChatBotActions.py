'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore.Action import Action
from ChatOS.Chatgets.ChatField import ChatField
from ChatOS.ChatCore.Intent import Intent
from ChatOS.ChatCore.ChatBot import ChatBot
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
            self.setOutput('Could you please tell me the name of the chatbot you want to create?')
            newSentence=super().exec(sentence)
            ccb.createChatBot(newSentence)
            self.setOutput("The chatbot named "+newSentence+" has been created.")
        except ChatExceptionScape as ces:
            return
        except ChatExceptionMisunderstand as cem:
            return
        
        
        self.chatBot.currentChatBot=ChatBot(self.chatBotName)
class NewIntent(Action):
    def __init__(self, chatBot):
        super(chatBot)
        self.intentName="no intent"
    def exec(self,sentence=""):
        self.chatBot.currentChatBot.intents[self.intentName]=Intent(self.chatBot.currentChatBot,self.intentName)
class NewPattern(Action):
    def __init__(self, chatBot):
        super(chatBot)
    def exec(self,sentence=""):
        pass
class NewResponse(Action):
    def __init__(self, chatBot):
        super(chatBot)
    def exec(self,sentence=""):
        pass
class NewAction(Action):
    def __init__(self, chatBot):
        super(chatBot)
    def exec(self,sentence=""):
        pass