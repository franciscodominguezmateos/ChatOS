'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''

class ChatException(Exception):
    def __init__(self, params):
        pass
class ChatExceptionScape(ChatException):
    pass
class ChatExceptionMisunderstand(ChatException):
    pass
