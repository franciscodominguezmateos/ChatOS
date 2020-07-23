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
        self.action   =None
        self.chatBot  =chatBot
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
        self.action=intent['action']
    def toJsonData(self):
        dic={}
        dic["name"]=self.name
        dic["patterns"]=self.patterns
        dic["responses"]=self.responses
        dic["action"]=self.action
        return dic
