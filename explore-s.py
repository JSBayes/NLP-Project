import pandas as pd
import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from prepare_readme import get_ASCII, purge_non_characters, prep_readme, basic_clean, tokenize
import seaborn as sns
import matplotlib.pyplot as plt
nltk.download("stopwords")
nltk.download("wordnet")
df = prep_readme()


def word_list(df):
    col = df.language.unique()
    final = pd.DataFrame()
    list_ = []
    for x in col:
        list2 = []
        for n in df.readme_contents_lemmatized.apply(tokenize)[df.language==x]:
            list2.extend(n)
        list_.append(list2)
    return list_

wl = word_list(df)
css = pd.DataFrame(pd.Series(wl[0]).value_counts())
java = pd.DataFrame(pd.Series(wl[1]).value_counts())
cplus = pd.DataFrame(pd.Series(wl[2]).value_counts())
c = pd.DataFrame(pd.Series(wl[3]).value_counts())
js = pd.DataFrame(pd.Series(wl[4]).value_counts())
shell = pd.DataFrame(pd.Series(wl[5]).value_counts())
python = pd.DataFrame(pd.Series(wl[6]).value_counts())
html = pd.DataFrame(pd.Series(wl[7]).value_counts())


