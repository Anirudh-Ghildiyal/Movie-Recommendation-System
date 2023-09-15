import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
  response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=e81dd9737aac1632c92c3216713e7831&language=en-US".format(movie_id))
  data = response.json()
  return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
  movie_index = movies[movies["title"] == movie].index[0]
  distance = similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)), reverse = True, key = lambda x:x[1])[1:6]

  recommended_movies = []
  recommended_movies_poster = []
  for i in movies_list:
    movie_id = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
    recommended_movies_poster.append(fetch_poster(movie_id))
  return recommended_movies, recommended_movies_poster

st.title("Movie Recommendation System")

movies_dict = pickle.load(open("movie_dict.pkl","rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl","rb"))
selected_movie_name = st.selectbox("Enter your movie",movies["title"].values)

if st.button("Recommend Movie"):
  names, posters = recommend(selected_movie_name)
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    st.text(names[0])
    st.image(posters[0], use_column_width=True)
  with col2:
    st.text(names[1])
    st.image(posters[1], use_column_width=True)
  with col3:
    st.text(names[2])
    st.image(posters[2], use_column_width=True)
  with col4:
    st.text(names[3])
    st.image(posters[3], use_column_width=True)
  with col5:
    st.text(names[4])
    st.image(posters[4], use_column_width=True)