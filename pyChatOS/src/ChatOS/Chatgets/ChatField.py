'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore.Action import Action
from ChatOS.ChatCore.ChatExceptions import ChatExceptionMisunderstand, ChatExceptionScape
import ChatOS.ChatIO as ChatIO

class ChatField(Action):
    def __init__(self, chatBot):
        super().__init__(chatBot)
        self.keywordsScape=["scape","flee","exit"]
        self.keywordsMisundertand=["misundentand","error"]
        self.input=ChatIO.input
    def exec(self,sentence):
        sentence=self.input.getInput()
        if sentence in self.keywordsScape:
            raise ChatExceptionScape()
        if sentence in self.keywordsMisundertand:
            raise ChatExceptionMisunderstand()
        return sentence