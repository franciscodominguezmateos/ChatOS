'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
import threading
from xmlrpc.server import SimpleXMLRPCServer
from ChatOS.ChatIO.ChatInput import ChatInput


class ChatInputVoice(ChatInput):
    '''
    Input string from XML call
    Output shell script to pico2wave
    '''
    def __init__(self,port=8001):
        """
        Constructor mainly for getInput
        """
        self.port=port
        self.iString=""
        thread = threading.Thread(target=self.xmlsvr, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def xmlsvr(self):
        """
        Server xml-rpc thread el thread.
        :return: void
        """
        server = SimpleXMLRPCServer(("", self.port))
        print("Listening on port %d..."%self.port)
        server.register_instance(self)
        server.serve_forever()

    def asr(self,s):
        """
        Additional check method.
        param s: remote command
        return: string: ok
        """
        print("Recibido ",s)
        self.iString=s
        return "ok-from ChatOS"
    
    def getInput(self):
        while self.iString=="":
            pass
        value=self.iString
        self.iString=""
        return value