# from __future__ import print_function
from nltk.stem import PorterStemmer
import numpy as np
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer

import textdistance
import fuzzy

soundex = fuzzy.Soundex(4)

lemmatizer = WordNetLemmatizer()

def cleanhtml(raw_html):
    #remove html tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    #remove punctuation
    punc = re.sub(r'[^\w\s]','',cleantext)
    #lowercase
    lowe=punc.lower()
    return lowe

stop_words = stopwords.words('english')
stemmer = SnowballStemmer("english")


with open("soccermom.txt", "r") as train_data:
    lines = train_data.readlines() 
    
with open("soccermom_genius.txt", "r") as test_data:
	lines2 = test_data.readlines()   

rating = []

new_corpus2=''
for l2 in lines2:
    #clean html in review
    cleaned=(cleanhtml(l2))
    #splice review into [] of words
    words=cleaned.split()
    new_text=""
    # print(words)
    for w in words:
        if w not in stop_words:
            x = lemmatizer.lemmatize(w)
            new_text=new_text+" "+x
    new_corpus2+=new_text
print(new_corpus2)

new_corpus=''
for l in lines:
    #clean html in review
    cleaned=(cleanhtml(l))
    #splice review into [] of words
    words=cleaned.split()

    # print(words)
    new_text=""
    for w in words:
        if w not in stop_words:
            x = lemmatizer.lemmatize(w)
            new_text=new_text+" "+x
    new_corpus+=new_text

print(new_corpus)

#get in same format
ugh=''
for line in new_corpus:
    ugh=ugh+line

# print(ugh)
# print(new_corpus2)


lev_dist=textdistance.levenshtein.normalized_similarity(new_corpus2,ugh)

dam_lev_dist=textdistance.damerau_levenshtein.normalized_similarity(new_corpus2,ugh)
soren_dist=textdistance.sorensen(new_corpus2.split(),ugh.split())

#genius
new_corpus2_s=''
for w in new_corpus2.split():
    s=soundex(w)
    new_corpus2_s+=' ' +s

#comput generated
ugh_s=''
for w in ugh.split():
    s=soundex(w)
    ugh_s+=' ' + s

#genius
x=set(new_corpus2_s.split())
x_len=len(x)
print(x)

#comput generated
y=set(ugh_s.split())
print(len(y))
print(y)

#genius-comput_generated=z
z=list(x-y)
print(z)

z_len=len(z)
print(z_len)
print(z_len/x_len)
# n=[item for item in x if item not in y]
# print(n)


# sound_lev=textdistance.damerau_levenshtein.normalized_similarity(new_corpus2_s,ugh_s)

# print(new_corpus2)
# print(ugh)

print(lev_dist)

print(dam_lev_dist)
print(soren_dist)

# print(sound_lev)