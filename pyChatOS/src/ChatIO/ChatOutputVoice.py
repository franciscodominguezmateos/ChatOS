'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
import os

from ChatIO.ChatOutput import ChatOutput

class ChatOutputVoice(ChatOutput):
    '''
    Output shell script to pico2wave
    '''    
    def setOutput(self,response):
        print(response)
        if type(response) is str:
            print(response)
            tosay=response.replace('"','')
            #command='~/di.sh  "%s."'%tosay
            command='~/say.sh  "%s."'%tosay
            os.system(command)