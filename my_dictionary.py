import json
import pyttsx3
from difflib import get_close_matches


engine = pyttsx3.init()
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # for female voice

data = json.load(open('data.json')) # load json data into python dictionary


yorn = 'y'

def word_meaning(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yorn  = input(f"Do you mean {get_close_matches(word,data.keys())[0]} instead?(y/n):")
        if yorn == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            print('\n Sorry!! this word is not in my dictionary!')
            engine.say('Sorry!! this word is not in my dictionary')
            engine.runAndWait()
            engine.stop()
    else:
        print('\n Sorry!! this word is not in my dictionary!')
        engine.say('Sorry!! this word is not in my dictionary')
        engine.runAndWait()
        engine.stop()


while(yorn == 'y'):
    word = input('Enter a word for the definition:\n').lower()

    definitions = word_meaning(word)
    if bool(definitions):
        for definition in definitions:
            print("\n",definition)
        engine.say(definitions)
        engine.runAndWait()
        engine.stop()
    yorn = input('Do you want to continue search (y/n):').lower()

    if yorn == 'n':
        exit()
