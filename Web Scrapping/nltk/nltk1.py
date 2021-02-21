# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 13:08:32 2020

@author: HP
"""
import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import word_tokenize


text='While details are awaited on the 12-hour-long meeting at the Corps Commander level between India and China, Army Chief Gen. Manoj Naravane is scheduled to visit Ladakh later on Tuesday to review the ground situation." Gen. Naravane will be visiting Ladakh for reviewing the ground situation, discuss the on-going stand-off with ground commanders, visit forward locations and interact with troops on the ground,” Army sources said. He will travel to Ladakh later in the day and be there on Wednesday. " '
text1='Part of Speech tagging does exactly what it sounds like, it tags each word in a sentence with the part of speech for that word. This means it labels words as noun, adjective, verb, etc. PoS tagging also covers tenses of the parts of speech. This is normally quite the challenge, but NLTK makes this pretty darn simple! '

#custom_sent= PunktSentenceTokenizer(text1)
custom_sent= PunktSentenceTokenizer(text1)
tokenized=custom_sent.tokenize(text)
print('--'*30)
print(tokenized)

len(tokenized)
print('*'*30)
print(text)
for sent in tokenized:
    print('--'*30)
    print(sent)
    print('--'*30)
    try:
        words= nltk.word_tokenize(sent)
        
        print(words)
        print('--'*30)
        tagged= nltk.pos_tag(words)
        print(tagged)
        break        
    except Exception as e:
        print(e)

























































