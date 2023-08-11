import streamlit as st
from utilities.database import get_anime_compacted_df, get_anime_country_df, get_anime_watch_df


st.write("General Idea Page..!")
st.write("Anime Compacted Shape: ", get_anime_compacted_df().shape)
st.write("Anime Country Shape: ", get_anime_country_df().shape)
st.write("Anime Watch Shape: ", get_anime_watch_df().shape)