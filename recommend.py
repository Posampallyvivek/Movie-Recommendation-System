import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import os

movies = pd.read_csv('/Users/venug/OneDrive/Desktop/Movie rcmd/movies.csv')
credits = pd.read_csv('/Users/venug/OneDrive/Desktop/Movie rcmd/credits.csv')

movies.head(2)

credits.head(2)

movies.shape

credits.shape

movies = movies.merge(credits , on = 'title')

movies.shape

movies.iloc[0]

movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

movies.head()

movies.shape

movies.isnull().sum()

movies.dropna(inplace=True)

movies.shape

movies.duplicated().sum()

movies.head(2)

movies.iloc[0]['genres']

import ast

def convert(text):
    l = []
    for i in ast.literal_eval(text):
        l.append(i['name'])
        
    return l

movies['genres'] = movies['genres'].apply(convert)

movies.head(2)

movies['keywords'] = movies['keywords'].apply(convert)

movies.head(2)

movies.iloc[0]['cast']

def convert(text):
    l = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            l.append(i['name'])
        counter +=1
        
    return l

movies['cast'] = movies['cast'].apply(convert)

movies.head(2)

movies.iloc[0]['crew']

def fetch_director(text):
    l = []
    for i in ast.literal_eval(text):
        if i['job']=='Director':
            l.append(i['name'])
            break
        
    return l

movies['crew'] = movies['crew'].apply(fetch_director)

movies.head(2)

movies.iloc[0]['overview']

movies['overview'] = movies['overview'].apply(lambda x:x.split())
movies.head()

movies.iloc[0]['overview']

def remove_space(word):
    l = []
    for i in word:
        l.append(i.replace(" ",""))
    return l

movies['crew'] = movies['crew'].apply(remove_space)
movies['cast'] = movies['cast'].apply(remove_space)
movies['keywords'] = movies['keywords'].apply(remove_space)
movies['genres'] = movies['genres'].apply(remove_space)

movies.head()

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] +movies['crew']

movies.head()

movies.iloc[0]['tags']

new_df = movies[['movie_id','title','tags']]

new_df.head()

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
new_df.head()

new_df.iloc[0]['tags']

new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())
new_df.head()

new_df.iloc[0]['tags']

import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def stems(text):
    l = []
    for i in text.split():
        l.append(ps.stem(i))
        
    return " ".join(l)

new_df['tags'] = new_df['tags'].apply(stems)

new_df.iloc[0]['tags']

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words= 'english')

vector = cv.fit_transform(new_df['tags']).toarray()

vector

vector.shape

from sklearn.metrics.pairwise import cosine_similarity

similary = cosine_similarity(vector)

similary

similary.shape

 new_df[new_df['title']=='Spider-Man'].index[0]

def recommend(movie):
    index = new_df[new_df['title']=='Spider-Man'].index[0]
    distances = sorted(list(enumerate(similary[index])), reverse=True, key = lambda x: x[1])
    for i in distances[1:6]:
        print(new_df.iloc[i[0]].title)

recommend('Spider-Man')
