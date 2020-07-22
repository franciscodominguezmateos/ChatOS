'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''

class ChatIO(object):
    '''
    classdocs
    '''
    def getInput(self):
        return input('Ready: ')
    def setOutput(self,response):
        print(response)
