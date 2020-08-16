'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
from ChatOS.ChatCore.ChatBot import ChatBot 
import ChatOS.ChatIO as ChatIO
from ChatOS.Chatgets.ChatConfirm import ChatConfirm

class ChatBotEngine(object):
    def __init__(self):
        chatbot=ChatBot('ChatDesktop') 
        self.chatbotStack=[chatbot]
        self.currentIntent="None"
        self.output=ChatIO.output
        self.input =ChatIO.input
    def getInput(self):
        return self.input.getInput()
    def setOutput(self,response):
        self.output.setOutput(response)
    def launchChatBot(self,chatBotName):
        chatbot=ChatBot(chatBotName)
        self.chatbotStack.append(chatbot)
    def getCurrentChatBot(self): 
        return self.chatbotStack[-1]    
    def notEmptyStack(self): return self.chatbotStack
    def popChatBot(self):
        if len(self.chatbotStack)==1:
            self.setOutput("This is the last chatbot. The system will be closed. Are you sure?")
            cfcg=ChatConfirm(self.getCurrentChatBot())
            response=cfcg.exec("")
            if response:
                self.setOutput("A pleasure serving you.Bye.")
            else:
                self.setOutput("Ok, go on talking.")
                return
        self.chatbotStack.pop()
    def run(self):
        while self.notEmptyStack():
            sentence=self.getInput()
            response,intentName=self.getCurrentChatBot().chat(sentence)
            self.currentIntent=intentName
            self.setOutput(response)
            if self.currentIntent!="goodbye":
                self.getCurrentChatBot().act(intentName, sentence)
            else: 
                self.popChatBot()
        self.currentIntent="None"
