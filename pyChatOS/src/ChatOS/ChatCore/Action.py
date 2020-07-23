'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''

class Action(object):
    '''
    Abstract class for actions associated to intents
    '''
    def __init__(self,chatBot):
        self.chatBot=chatBot
    def exec(self,sentence=""):
        '''
        All actions have to have this execution method 
        '''
        pass