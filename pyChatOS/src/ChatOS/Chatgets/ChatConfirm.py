'''
Created on 28 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore.Action import Action
from ChatOS.ChatCore.ChatExceptions import ChatExceptionMisunderstand, ChatExceptionScape
import ChatOS.ChatIO as ChatIO

#This could inherit from ChatField
class ChatConfirm(Action):
    def __init__(self, chatBot):
        super().__init__(chatBot)
        self.confirmWords=["yes","sure","true" ,"confirm","ok","one"]
        self.cancelWords =[ "no",       "false","cancel" ,"ko","zero"]
        self.keywordsScape=["scape","flee","exit"]
        self.keywordsMisundertand=["misundentand","error"]
        self.input=ChatIO.input
    def exec(self,sentence):
        sentence=self.input.getInput()
        if sentence in self.keywordsScape:
            raise ChatExceptionScape()
        if sentence in self.keywordsMisundertand:
            raise ChatExceptionMisunderstand()
        if sentence in self.confirmWords:
            return True
        if sentence in self.cancelWords:
            return False
        #What TODO in this case?