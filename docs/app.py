import streamlit as st

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import pandas as pd


# Page Configuration
st.set_page_config(
    page_title="Anime Quest",
    page_icon="docs/icons/anime_quest_icon.png",
    menu_items={
        'About': "This is about section..!",
        'Report a bug': "https://github.com/MYTE21/Anime.Quest/issues/new",
    }
)


# Connection Initialization
@st.cache_resource
def initialize_connection():
    username = st.secrets["username"]
    password = st.secrets["password"]
    cluster_name = st.secrets["cluster_name"]

    uri = f"mongodb+srv://{username}:{password}@{cluster_name}.yomhl8y.mongodb.net/?retryWrites=true&w=majority"
    return MongoClient(uri, server_api=ServerApi('1'))


client = initialize_connection()


# Pull Data From Collection
@st.cache_resource
def get_dataframe():
    db = client["anime_quest"]

    # Collections
    collection_compacted = db["anime_compacted"].find()
    collection_country = db["anime_country"].find()
    collection_watch = db["anime_watch"].find()

    # Pandas DataFrame Conversion
    dataframe_anime_compacted = pd.DataFrame(collection_compacted)
    dataframe_anime_country = pd.DataFrame(collection_country)
    dataframe_anime_watch = pd.DataFrame(collection_watch)

    return dataframe_anime_compacted, dataframe_anime_country, dataframe_anime_watch


df_anime_compacted, df_anime_country, df_anime_watch = get_dataframe()

st.dataframe(df_anime_compacted)
st.dataframe(df_anime_country)
st.dataframe(df_anime_watch)


st.write("DONE..!")
