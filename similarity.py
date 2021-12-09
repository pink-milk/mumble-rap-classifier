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

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')
def clean(text):
    
    #remove punctuation
    punc = re.sub(r'[^\w\s]','',text)
    #lowercase
    lowe=punc.lower()
    return lowe

genius="genius_jcole.txt"
comput="jcole.txt"

with open(comput, "r") as train_data:
    comput_lines = comput.readlines()
    
with open(genius, "r") as test_data:
	genius_lines = genius.readlines()   
