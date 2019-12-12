# NLP-Project

In this project we will attempt to identify the main programming language being used in a given github repository, by preforming Natural Language Processing on the contents of that repositories README file. 

NLP Project

For this project, you will be scraping data from GitHub repository README files. The goal will be to build a model that can predict what programming language a repository is, given the text of the README file.

Deliverables

A well-documented jupyter notebook that contains your analysis
One or two google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.
Guidance

Acquisition + Preparation

For this project, you will have to build a dataset yourself. Decide on a list of GitHub repositories to scrape, and write the python code necessary to extract the text of the README file for each page, and the primary language of the repository.

You can find the language of a repository like this:



Note that the gif above shows how to do this in your browser, you'll need to come up with a solution in Python.

Which repositories you use are up to you, but you should include at least 100 repositories in your data set.

As an example of which repositories to use, here is a link to GitHub's trending repositories, the most forked repositores, and the most starred repositories.

Exploration

Explore the data that you have scraped. Here are some ideas for exploration:

What are the most common words in READMEs?
What does the distribution of IDFs look like for the most common words?
Does the length of the README vary by programming language?
Do different programming languages use a different number of unique words?
Modeling

Transform your documents into a form that can be used in a machine learning model. You should use the programming language of the repository as the label to predict.

Try fitting several different models and using several different representations of the text (e.g. a simple bag of words, then also the TF-IDF values for each).

Build a function that will take in the text of a README file, and tries to predict the programming language.