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
from prepare_readme import get_ASCII, purge_non_characters, prep_readme, basic_clean, tokenize
import seaborn as sns
import matplotlib.pyplot as plt
nltk.download("stopwords")
nltk.download("wordnet")
origin_df = prep_readme()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

tfidf = TfidfVectorizer(ngram_range=(1,2))
tfidfs = tfidf.fit_transform(origin_df.readme_contents_lemmatized)
X = tfidfs
y = origin_df.language
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.5)



from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier

lm = RandomForestClassifier(random_state=123, min_samples_split=10,\
     n_estimators=1000,n_jobs=-1)
lm.fit(X_train, y_train)
lm.score(X_train, y_train)
lm.score(X_test, y_test)
origin_df.language.value_counts()

