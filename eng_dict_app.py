# Intelligent Dictionary
'''
-->A Normal Dictionary gives you the meaning of word what you enter,
-->If the dictionary doesn't have that word, It doesn't show you anything. But,
-->This Intelligent Dictionary suggests a word that closes to what you've entered!(Interesting...)
'''

import json
from difflib import get_close_matches

data = json.load(open("dict_data.json"))

def intelligent_dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn in ["Y","y"]:
        
            return data[get_close_matches(w, data.keys())[0]]
        if yn in ["N","n"]:
            return "Sorry,No matches in this Dictionary. Please try again."

        else:
            return "Sorry,No matches in this Dictionary. Please try again."
    else:
        return "Sorry,No matches in this Dictionary. Please try again."

word = input("Enter word: ") 
output = intelligent_dictionary(word)
if type(output) == list:
    for meaning in output:
        print(meaning)
else:
    print(output)

#Happy Coding
