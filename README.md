# ChatOS
Chatbot Operative System

This is a low level chatbot operative system analogous to traditional GUI. You need to get used to it. Its goal is not accure prediction and understanding of Natural Language, but a practical tool to interact with different system, mainly robots and autonomous systems.
Some visual information can be used in order to support the interaction.
It could be interesting take out information from sentences and pass then to actions or to the chatgets

Most of this chatbots are passive, for a more natural interaction some kind of proactive or active chatbots would be figured out, as one that ask you for information.

Analogous to traditional GUI, ChatOS has a desktop, ChatDesktop, wingets, Chatgets and a development enviroment, MetaChatBot.

There are global intents in order to exit, or inform of error to ChatLearner (ChatGlobal)

It aim to be input/output independent it can be used text, keyboard or voice and Language Processing independent it can work with NLP of high level, traditional parser, regular expression or just keywords.

NLPModel -> Natural Language Processing model it can be a neural network, a parser, 

NLPModelBoW -> This is a NLPModel for Bag of Words with Artificial Neural Networks
NLPModelKeyWords -> this is just a keywords chat bot ther patters are keyword that the sentence has to have in order to detect the intent.
NLPModelRegEx -> use a regexp to match sentences and pattern.
NLPModelMix -> this could be a combination of different NLPModel for instance it could use a BoW for have a natural interaction but pick up numbers or date from the sentence with some king of regular expression

NLPANN -> abstraction of Artificial Neural Networks to do NLP platform independent

NLPANNkeras -> An ANN in keras it is just a MLP it is used in NLPModelBoW

Intent -> ChatOS is based in chatbots type intention guessing

ChatBot -> A chatbot is a collection of intent and a model to guess intents, and ejecute the associated action to the intent. It could extract information and pass it to the action.

ChatBotEngine ->

## Chatget 
These are analogous to winget for GUI, actually they are minichatbots with a output, they are going to be called from the action mostly.
Most of the chatget can have the option of confirmation, after the information if filled the system read it and ask for confirmation.
- ChatDate, ChatTime, ChatDateTime
- ChatMonth, ChatWeekDay, ChatNumber
- ChatField
 just ask for a sentence
- ChatLines
 read a collection of sentences up to a keywork "exit/finish/stop". Imagine you want to add a list of fruit to your shoping list, instead of adding fruit by fruit you would add a list.
 A variant of this is that the sentences or fruit in the anterior example has to be in a list of fruits, that could allow control error.
- ChatText
 ask for a number of sentences and a keywork "exit/full stop" to finish.
 This can have some keywords to format the input as "dot/point/coma"
- ChatOptions
 You can choose one option from a list of optons by name or by number
- ChatCheck
 You can choose many option from a list of options by name or by number
- ChatForm
 ask for a number of fields but:
 - with 'scape/exit' you leave the form
 - with 'save and exit/scape' you save the form ane leave the form
 - with 'next' left empty this field and go to next field
 - ¿What if the information from the ASR is wrong?-> 'backward/previous field' take you to the previous field
 There may be a version where it only ask empty fields, this could be a ChatFormToComplete....
 After the last field it can read all information and ask for 'cancel/no' 'confirm/ok/yes/fine'

## ChatDesktop
This is analogous to desktop GUI
Direct link
 given a pattern it jump to a chatbot with a intent, this has two optons:
  - continue in thet chatbot
  - just return after the action associated to the intent is executed
Open a chatbot
ChatNavigator
 - Ask for the chatbots available
 - download chatbots
 - install/uninstall chatbots
Global NLPModel
ChatDesktop can have a global NLP model able to discriminate chatbots and intent, it could train a model with all pattern of all chat bots and as output a pair (chatbot, intent) -> this could be used on direct links

## MetaChatBot
A chatbot to build or modify other chatbots, but a lot of work have to be done manually. As programing the actions, the NLPModels,... etc.

## ChatLearner
Detect prediction error an improve the model of chatbots
Or at any moment the user can uterate a command as "save last sentence" and the last sentence will be saved to improve the NLP model.

## ChatHelp
Give you information about some chatbot

## ChatGlobal
It is a chat with intents common to all chatbots, all chatbots have the intents in the json file and the global intents
- As for help
  - What is this chat?
  - What intents can I use?
- escape/exit/return
  - it stop the actual chatbot an return to ChatDektop
- Error/mistake/misundestanding
  - when the detector doesn't recognize the right intent this can ask to save the sentence in order to later run ChatLearner in order to improve the system adding the sentece to the list of patter in the right intent. When teh sentence is saved, the failled intent is saved and the chatbots.
- saveLastSentence
 will save last utterated sentence in order to allow ChatLearner improve the model
- i don't understand
   - When the NLP can't detect the intent this is the intent to be launch, it will sample from response as a reply

## user, roles and grants
it could be useful tu have different users as guest, root, developer, etc.

## Applications
ChatOS aim is to be the support for the interaction with a very simple knolendge system in robots. 
with some kind of object, properties, categories/classes and relations and a basic bayesian inference model engine to make some kind of reasoning.
There is going to be: 
 ChatKnoledge that fill information with interaction with users.
  - This interaction can be just speaking or
  - Through vision, for instance the user can teach new objects to the robot pointing to them with the index finger tip and telling to the chatbot what object it is. After a number of samples it could train a object recognizer/detector.
 ChatBayesianNetwork, to build bnn and reason with them and associate them with the knoledge system. For instance we can define a bnn for illnesses detection and associate to some instance of the class Person given some especific evidences of that person. This can give rise to some infered fields.
 
 A easy esample would be a chatbot to guess and animal given some properties. It could ask properties from the animal and try to guess witch animal is it.

- To interact with git?

