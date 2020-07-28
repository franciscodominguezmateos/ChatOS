'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
import random
class Intent(object):
    def __init__(self,chatBot,name=""):
        self.name     =name
        self.patterns =[]
        self.responses=[]
        self.actionName   =""
        self.chatBot  =chatBot
    def getName(self): return self.name
    def getActionName(self):
        return self.actionName
    def chooseResponse(self):
        sizeResponses   = len(self.responses)
        chooseIdResponse= random.randint(0,sizeResponses-1)
        response        = self.responses[chooseIdResponse]
        return response
    def fromJsonData(self,intent):
        self.patterns =[]
        self.responses=[]
        self.name=intent['name']
        for pattern in intent['patterns']:
            self.patterns.append(pattern)
        for response in intent['responses']:
            self.responses.append(response)
        self.actionName=intent['actionName']
    def toJsonData(self):
        dic={}
        dic["name"]=self.name
        dic["patterns"]=self.patterns
        dic["responses"]=self.responses
        dic["actionName"]=self.actionName
        return dic
