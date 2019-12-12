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
origin_df = prep_readme()


def word_list(origin_df):
    col = df.language.unique()
    final = pd.DataFrame()
    list_ = []
    for x in col:
        list2 = []
        for n in df.readme_contents_lemmatized.apply(tokenize)[df.language==x]:
            list2.extend(n)
        list_.append(list2)
    return list_

wl = word_list(origin_df)
css = pd.DataFrame(pd.Series(wl[0]).value_counts()).rename(columns={0:"css"}).reset_index()
java = pd.DataFrame(pd.Series(wl[1]).value_counts()).rename(columns={0:"java"}).reset_index()
cplus = pd.DataFrame(pd.Series(wl[2]).value_counts()).rename(columns={0:"cplus"}).reset_index()
c = pd.DataFrame(pd.Series(wl[3]).value_counts()).rename(columns={0:"c"}).reset_index()
js = pd.DataFrame(pd.Series(wl[4]).value_counts()).rename(columns={0:"js"}).reset_index()
shell = pd.DataFrame(pd.Series(wl[5]).value_counts()).rename(columns={0:"shell"}).reset_index()
python = pd.DataFrame(pd.Series(wl[6]).value_counts()).rename(columns={0:"python"}).reset_index()
html = pd.DataFrame(pd.Series(wl[7]).value_counts()).rename(columns={0:"html"}).reset_index()
df = css.merge(java, how="outer", on="index")
df = df.merge(cplus, how="outer", on="index")
df = df.merge(c, how="outer", on="index")
df = df.merge(js, how="outer", on="index")
df = df.merge(shell, how="outer", on="index")
df = df.merge(python, how="outer", on="index")
df = df.merge(html, how="outer", on="index")
df.set_index("index", inplace=True)
df.fillna(0, inplace=True)
df["all"] = df.sum(axis=1)

(df
 .assign(css=df.css / df['all'],
         java=df.java / df['all'],
         cplus=df.cplus/ df["all"],
         c=df.c/df['all'],
         js=df.js/df['all'],
         shell=df.shell/df['all'],
         python=df.python/df['all'],
         html=df.html/df['all'],)
 .sort_values(by='all')
 [['css', 'java', "cplus", "c", "js", "shell", "python", "html"]]
 .tail(20)
 .sort_values('all')
 .plot.barh(stacked=True))




