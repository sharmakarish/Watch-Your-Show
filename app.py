from email.mime import image
import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config (layout="wide")
activities = ["ABOUT PROJECT", "CONTACT ME", "ABOUT ME"]
choice  = st.sidebar.selectbox("Project Details Section", activities)

if choice == 'ABOUT PROJECT':

    st.sidebar.write("Watch My Show - ")
    st.sidebar.write("This is a movie Recommendation System based on the function that when you select an movie then it will recommend 5 movies which are similar to genre or title of the selected movie. ") 
    st.sidebar.write("Tech Stack used - Python , Streamlit  ")


elif choice == 'CONTACT ME':
    st.sidebar.write("Get in touch with me!")

    col1,col2 = st.columns(2)
    with col1:
     
        st.sidebar.write("[LinkedIn Profile](https://www.linkedin.com/in/karishmasharma07)")
        st.sidebar.write("[Github Profile]( https://github.com/sharmakarish)")
        st.sidebar.write("ghoshikarishma1@gmail.com")

elif choice == 'ABOUT ME':
    col1, mid, col2 = st.columns([1, 1, 20])

    with col1:
        st.sidebar.image('https://i.postimg.cc/4xfPdBSX/karish-modified.png',width= 200)
        st.sidebar.write("Hi I am Karishma Sharma ,a sophomore at MBM engineering college jodhpur, currently pursuing Bachelor's of Engineering in Information Technology, who strongly believes in perseverance and patience,I am an avid leaner driven by desire to learn more and more skills and technologies.I have my interests in designing, web development and am skilled with tech stack like front end web development and with a learning mind having an aim to serve the nation .")

# ---------------CAROUSEL------------------------------------------------------------------
col1,col2, col3 = st.columns(3)
with col1 : st.image("https://th.bing.com/th/id/OIP.rDPmO2Rnm6uQ1b98VlUJUgHaEK?w=320&h=180&c=7&r=0&o=5&dpr=1.54&pid=1.7")
with col2 : st.image("https://i.postimg.cc/mDX8fMwT/logo.png" , "See What's Next!")
with col3 : st.image("https://th.bing.com/th/id/OIP.jzBrlFmYjcggAeePuaig_AHaEo?pid=ImgDet&rs=1")

# Creating a function to fetch poster from API ----------------------------------------------
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

movie_list = pickle.load(open('movie_dict.pkl', 'rb'))

movies = pd.DataFrame(movie_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# content---------------------------------------------------------------------
st.markdown("<h1 style='text-align: center; color:#FFFFFF; font: Serif'> MOVIE RECOMMENDATION SYSTEM</h1>", unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col2 :
    st.write('Hello and Welcome to Watch_Your_Show.com!!! ')

st.write('This website basically works on movie recommendation system which suggests you movies of same genre that you have chosen . ')

selected_movie_name = st.selectbox(
    'Select a movie',
    movies['title'].values)

if st.button('Recommend'):

    recommended_movie_names,recommended_movie_posters= recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.header(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.header(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])


    with col4:
        st.header(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
       
    with col5:
        st.header(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
