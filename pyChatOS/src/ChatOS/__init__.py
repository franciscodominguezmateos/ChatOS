'''
Created on 28 Jul 2020

@author: Francisco Dominguez
'''
import os

from ChatOS.ChatCore.ChatBotEngine import ChatBotEngine

BASE_PATH=os.path.join('.','ChatOS')
BASE_PATH_CHATBOTS=os.path.join(BASE_PATH,'ChatBots')
#CURRENT_LANG='en-GB'
#CURRENT_LANG='es-ES'
CURRENT_LANG=''
chatBotEngine=ChatBotEngine()