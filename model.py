import pandas as pd
import unicodedata
import re
import json
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from prepare import get_ASCII, purge_non_characters, basic_clean, prep_readme
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
origin_df = prep_readme()
origin_df.drop(columns=["repo", "readme_contents", "readme_contents_lemmatized"], inplace=True)
tfidf = TfidfVectorizer(ngram_range=(1,1))
tfidfs = tfidf.fit_transform(origin_df.readme_contents_stemmed)
X = tfidfs
y = origin_df.language
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.5)


from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, ExtraTreesClassifier
rfc = RandomForestClassifier(random_state=123, min_samples_split=11,\
     n_estimators=100,n_jobs=-1, max_features="auto")
clf = AdaBoostClassifier(n_estimators=15,learning_rate=2,\
     random_state=123, base_estimator=rfc)
clf.fit(X_train, y_train)
clf.score(X_test, y_test)


from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3, n_jobs=-1)
neigh.fit(X_train, y_train)
neigh.score(X_test, y_test)





