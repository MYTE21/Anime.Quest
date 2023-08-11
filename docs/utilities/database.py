import streamlit as st
import pandas as pd
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


# Database Connection Initialization
@st.cache_resource
def initialize_connection():
    username = st.secrets["username"]
    password = st.secrets["password"]
    cluster_name = st.secrets["cluster_name"]

    uri = f"mongodb+srv://{username}:{password}@{cluster_name}.yomhl8y.mongodb.net/?retryWrites=true&w=majority"
    return MongoClient(uri, server_api=ServerApi('1'))


client = initialize_connection()


@st.cache_resource
def get_database():
    return client["anime_quest"]


@st.cache_resource
def get_anime_compacted_df():
    db = get_database()
    collection_compacted = db["anime_compacted"].find()
    dataframe_anime_compacted = pd.DataFrame(collection_compacted)
    return dataframe_anime_compacted


@st.cache_resource
def get_anime_country_df():
    db = get_database()
    collection_country = db["anime_country"].find()
    dataframe_anime_country = pd.DataFrame(collection_country)
    return dataframe_anime_country


@st.cache_resource
def get_anime_watch_df():
    db = get_database()
    collection_watch = db["anime_watch"].find()
    dataframe_anime_watch = pd.DataFrame(collection_watch)
    return dataframe_anime_watch
