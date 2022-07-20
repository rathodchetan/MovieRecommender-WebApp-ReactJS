import numpy as np
import pandas as pd
import ast
import json
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
    L = []
    for i in text.split():
        L.append(ps.stem(i))
    return " ".join(L)

def convertToList(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 

def convertToListCast(text):
    L = []
    count=0
    for i in ast.literal_eval(text):
        if count==3:
            break
        L.append(i['name']) 
        count+=1
    return L 

def convertToListDirector(text):
    L = []
    
    for i in ast.literal_eval(text):
        if i["job"]=="Director":
            L.append(i['name']) 
            break
    return L 

def removeSpace(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1

movies = pd.read_csv("movies.csv")
credits = pd.read_csv("credits.csv")

movies = movies.merge(credits,on='title')
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

movies['genres'] = movies['genres'].apply(convertToList)
movies['keywords'] = movies['keywords'].apply(convertToList)
movies['cast'] = movies['cast'].apply(convertToListCast)
movies['crew'] = movies['crew'].apply(convertToListDirector)
movies.dropna(inplace=True)

movies['cast'] = movies['cast'].apply(removeSpace)
movies['crew'] = movies['crew'].apply(removeSpace)
movies['genres'] = movies['genres'].apply(removeSpace)
movies['keywords'] = movies['keywords'].apply(removeSpace)

movies["overview"] = movies["overview"].apply(lambda x:x.split())
movies['tag'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new_df = movies.drop(columns=['overview','genres','keywords','cast','crew'])
new_df['tag'] = new_df['tag'].apply(lambda x: " ".join(x))
new_df = new_df.reset_index()
new_df['tag'] = new_df['tag'].apply(lambda x: x.lower())
new_df['tag'] = new_df['tag'].apply(stem)

cv = CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(new_df['tag']).toarray()

similarity = cosine_similarity(vector)

def movieRecommender(movie):
    index = new_df[new_df['title'] == movie].index[0]
    sorted_list = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x : x[1]) 
    for i in sorted_list[1:6]:
        print(new_df.iloc[i[0]].title)

movieRecommender("Gandhi")
movie_df = new_df.drop(columns=['index','tag'])

# movie_dict=movie_df.to_dict()

# poster_path=[]
# # poster_path = []
# for i in movie_dict['movie_id']:
# #     print(movie_dict['movie_id'][i])
#     mid=movie_dict['movie_id'][i]
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(mid))
#     if response.status_code == 200:
#         data = response.json()['poster_path']
#         if data==None:
#             data='http://www.movienewz.com/img/films/poster-holder.jpg'
#         poster_link = "https://image.tmdb.org/t/p/w500" + data
#         poster_path.append(poster_link)
#     else:
#         poster_path.append('http://www.movienewz.com/img/films/poster-holder.jpg')

# movie_df['poster']=poster_path
# movie_dict=movie_df.to_dict()

poster = pd.read_csv("poster.csv")
poster = poster.drop(columns=['Unnamed: 0'])
print(poster.head())
movie_dict=poster.to_dict()
with open('test.json', 'w') as f:
    json.dump(movie_dict, f)
sim_data = list(enumerate(similarity))



dict_val={}
for i in sim_data:
    sorted_list = sorted(list(enumerate(i[1])),reverse=True,key = lambda x : x[1])
#     print(sorted_list[1:6])
    dict_val[i[0]]=sorted_list[1:6]

with open('similarity.json', 'w') as f:
    json.dump(dict_val, f)