'''
Created on 22 Jul 2020

@author: francisco
'''
from ChatCore.Action import Action
from ChatCore.Intent import Intent
from ChatCore.ChatBot import ChatBot

class NewChatBot(Action):
    def __init__(self, chatBot):
        super(chatBot)
        self.chatBotName="unnamed"
    def exec(self,sentence=""):
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