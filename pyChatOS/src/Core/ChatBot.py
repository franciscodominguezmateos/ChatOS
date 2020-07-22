'''
Created on 22 Jul 2020

@author: Francisco Dominguegz
- it loads intent from ChatBotGlobal, these are intents shared by all chatbots
TODO: process actions
'''
import os
import json
import random
from Core.Intent import Intent
from NLPModels.NLPModelsBoW.NLPModelBoW import NLPModelBoW
class ChatBot(object):
    def __init__(self,name):
        self.name=name
        self.intents={}
        self.model=NLPModelBoW()
        self.model.setChatBot(self)
        #TODO: refactor this
        self.loadJson()
        self.model.load()
        self.predict_threshold=0.55
    def getBasePath(self):
        basePath=os.path.join('.','ChatBots',self.name)
        return basePath
    def getBaseFileName(self):
        baseFileName=os.path.join(self.getBasePath(),self.name)
        print("baseFileName=",baseFileName)
        return baseFileName
    def loadJson(self):
        self.intents={}
        fileName=os.path.join(self.getBaseFileName()+'.json')
        with open(fileName) as json_data:
            intents = json.load(json_data)
        # loop through each sentence in our intents patterns
        for intent in intents['intents']:
            iobj=Intent(self)
            iobj.fromJsonData(intent)
            self.intents[iobj.name]=iobj
        self.loadChatBotGlobal()
        self.model.buildData()
    def loadChatBotGlobal(self):
        if self.name=="ChatBotGlobal":
            return
        cbg=ChatBot("ChatBotGlobal")
        #just copy intents
        for ik in cbg.intents:
            self.intents[ik]=cbg.intents[ik]
            self.intents[ik].chatBot=self
    def saveJson(self):
        dic={}
        dic["name"]=self.name
        dic["intents"]=[self.intents[ik].toJsonData() for ik in self.intents]
        json_string=json.dumps(dic,indent=4)
        fileName=os.path.join(self.getBaseFileName()+'0.json')
        with open(fileName, 'w') as json_file:
            json_file.write(json_string)
    def chooseRandom(self,responses):
        sizeResponses=len(responses)
        chooseIdResponse=random.randint(0,sizeResponses-1)
        return responses[chooseIdResponse]
    #def chooseResponse(self,predictedIntent):
    #    for intent in self.intents:
    #        if intent.name==predictedIntent:
    #            return self.chooseRandom(intent.responses)
    def act(self,intent,sentence):
        pass
    def predictIntent(self,sentence):
        predicted_intent_name,idc,pc=self.model.predictClass(sentence)
        print(idc,predicted_intent_name,pc)
        if pc<self.predict_threshold:
            #this is a global intent
            predicted_intent_name="unknown"
        return self.intents[predicted_intent_name]
    def chat(self,sentence):
        intent  =self.predictIntent(sentence)
        response=intent.chooseResponse()
        return response,intent.name