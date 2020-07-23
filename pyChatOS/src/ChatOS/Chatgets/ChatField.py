'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore.Action import Action
from ChatOS.ChatCore.ChatExceptions import ChatExceptionMisunderstand, ChatExceptionScape

class ChatField(Action):
    def __init__(self, chatBot):
        super(chatBot)
        self.keywordsScape=["scape","flee"]
        self.keywordsMisundertand=["misundentand","error"]
    def exec(self,sentence):
        sentence=self.input.getInput()
        if sentence in self.keywordsScape:
            raise ChatExceptionScape()
        if sentence in self.keywordsMisundertand:
            raise ChatExceptionMisunderstand()