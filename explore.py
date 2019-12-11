def get_words(text):
    
    words = re.sub(r'[^\w\s]', '', text).split()
    return words

def get_ngrams(n=2):

    ngram_master_list = []

    for row in df.readme_contents_stemmed.apply(get_words):

        bigrams = nltk.ngrams(row, n)

        ngram_master_list.extend(bigrams)
    
    return ngram_master_list
    

def get_ngram_strings(ngrams):
    
    string_list = []

    for pair in ngrams:
    
        first = pair[0]

        second = pair[1]
    
        string_list.append(f"{first} {second}")
        
    return string_list