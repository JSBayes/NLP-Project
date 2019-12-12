import re
import unicodedata
import pandas as pd
import nltk

def word_soup(text):
    
    wnl = nltk.stem.WordNetLemmatizer()
 
    words = re.sub(r'[^\w\s]', '', text).split()
    return [word for word in words]

def get_ngrams(df,n=2):

    ngram_master_list = []

    for row in df.readme_contents_stemmed.apply(get_words):

        bigrams = nltk.ngrams(row, n)

        df_ngram_list.extend(bigrams)
    
    return ngram_master_list
    

def get_ngram_strings(ngrams):
    
    string_list = []

    for pair in ngrams:
    
        first = pair[0]

        second = pair[1]
    
        string_list.append(f"{first} {second}")
        
    return string_list