'''
Created on 22 Jul 2020

@author: Francisco Dominguez
'''
import os
import random
import pickle
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer

from NLPModels import NLPModel

class NLPANN(object):
    pass

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import load_model
class NLPANNkeras(NLPANN):
    def __init__(self,nlpModel):
        self.nlpModel=nlpModel
        self.ann=None
    def train(self,train_x,train_y):
        self.ann = Sequential()
        self.ann.add(Dense(25, input_dim=train_x.shape[1]))     # densidad de la primera capa de neurona y tipo de entrada
        self.ann.add(Dropout(0.5))                                   # convierte a 0 la mitad de 1 en el entrenamiento
        self.ann.add(Dense(25))                                      # densidad de la primera capa de neurona
        self.ann.add(Dropout(0.5))                                   # convierte a 0 la mitad de 1 en el entrenamiento
        self.ann.add(Dense(train_y.shape[1], activation='softmax'))  # densidad de la salida
        self.ann.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
        #self.ann.build()
        self.ann.summary()
        self.ann.fit(train_x, train_y, epochs=500, batch_size=train_x.shape[0])   # entrena el modelo
    def save(self,filename):
        self.ann.save(filename)
    def load(self,filename):
        self.ann = load_model(filename)
    def predict(self,sentenceBow):
        p=self.ann.predict(np.reshape(sentenceBow,(1,-1)))
        return p
class NLPModelBoW(NLPModel):
    def __init__(self):
        # Bag of Words data
        self.stemmer = LancasterStemmer()
        self.words=[]
        self.classes=[]
        self.documents=[]
        self.ignore_words=['?','.',',','!']
        # MLP data (this could be in a different object)
        self.ann=NLPANNkeras(self)
        self.train_x = []
        self.train_y = []
    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def clean_up_sentence(self,sentence):
        # tokenize the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [self.stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words
    def bow(self,sentence, show_details=False):
        # tokenize the pattern
        sentence_words = self.clean_up_sentence(sentence)
        # bag of words
        bag = []
        # create our bag of words array
        for w in self.words:
            bag.append(1) if w in sentence_words else bag.append(0)
        return(np.array(bag))
    def buildData(self):
        self.buildBowData()
        self.buildTrainingData()
    def buildBowData(self):
        self.words=[]
        self.classes=[]
        self.documents=[]
        for ik in self.chatBot.intents:
            intent=self.chatBot.intents[ik]
            for pattern in intent.patterns:
                # tokenize each word in the sentence
                w = nltk.word_tokenize(pattern)
                # add to our words list
                self.words.extend(w)
                # add to documents in our corpus
                self.documents.append((pattern, intent.name))
                # add to our classes list
                if intent.name not in self.classes:
                    self.classes.append(intent.name)
        # stem and lower each word and remove duplicates
        self.words = [self.stemmer.stem(w.lower()) for w in self.words if w not in self.ignore_words]
        self.words = sorted(list(set(self.words)))

        # remove duplicates
        self.classes = sorted(list(set(self.classes)))

        print (len(self.documents), "documents")
        print (len(self.classes), "classes", self.classes)
        print (len(self.words), "unique stemmed words", self.words)
    def buildTrainingData(self):
        # create our training data
        training = []
        output = []
        # create an empty array for our output
        output_empty = [0] * len(self.classes)

        # training set, bag of words for each sentence
        x=[]
        y=[]
        for doc in self.documents:
            # initialize our bag of words
            bag = self.bow(doc[0])
            x.append(bag)
            # output is a '0' for each tag and '1' for current tag
            output_row = list(output_empty)
            output_row[self.classes.index(doc[1])] = 1
            y.append(output_row)
        # shuffle our features and turn into np.array
        random.shuffle(training)
        training = np.array(training)
        print(training.shape)

        # create train data
        self.train_x = np.array(x)
        self.train_y = np.array(y)
    def train(self):
        self.ann.train(self.train_x,self.train_y)
    def save(self):
        # save all of our data structures
        data={}
        data['words']    =self.words 
        data['classes']  =self.classes 
        data['documents']=self.documents 
        data['train_x']  =self.train_x 
        data['train_y']  =self.train_y
        pickle.dump( data, open( os.path.join('./',self.chatBot.name+".pk"), "wb" ) )
        self.ann.save(os.path.join('./',self.chatBot.name+'.h5'))    # guarda el modelo
    def load(self):
        data = pickle.load( open( os.path.join('./',self.chatBot.name+".pk"), "rb" ) )
        self.words     = data['words']
        self.classes   = data['classes']
        self.documents = data['documents']
        self.train_x   = np.array(data['train_x'])
        self.train_y   = np.array(data['train_y'])
        self.ann.load(os.path.join('./',self.chatBot.name+'.h5'))
    def predictClass(self,sentence):
        sentenceBow=self.bow(sentence)
        p=self.ann.predict(sentenceBow)
        idClass=np.argmax(p)
        pClass=np.max(p)
        className=self.classes[idClass]
        return className,idClass,pClass
    
    
    
    
    
    
    