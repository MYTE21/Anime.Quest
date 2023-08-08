import streamlit as st
import pandas as pd
from PIL import Image

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from streamlit_extras.app_logo import add_logo
from streamlit_extras.mention import mention

# Page Configuration
st.set_page_config(
        page_title="Anime Quest",
        page_icon="docs/icons/anime_quest_icon.png",
        menu_items={
            'About': "This is about section..!",
            'Report a bug': "https://github.com/MYTE21/Anime.Quest/issues/new",
        }
    )


st.header("Anime Quest")
add_logo("docs/icons/anime_quest_icon.png", height=3)
image = Image.open("assets/anime_theme.jpg")
st.image(image)

"""
[Anime](https://en.wikipedia.org/wiki/Anime) is a distinct type of animation that features distinctive storytelling, 
creative sensibilities, and cultural allegiances, making it a well-liked and significant form of entertainment all 
around the world. It was created in Japan and has since spread throughout the world.

**What Is `Anime Quest`, though? 🤔**

It's a treasure of the anime world 🪙... Just kidding 😂… 

This public project is called `Anime Quest`, which used the [Selenium Python](https://selenium-python.readthedocs.io/) 
to extract anime information from the [Anime Planet](https://anime-planet.com/) website. After processing the dataset,
[Tableau Public](https://public.tableau.com/app/discover) is used to produce visualizations.
"""

# st.divider()

"""
### Other Parts of this Project
"""

github_column, kaggle_column, tableau_column = st.columns(3)
with github_column:
    mention(
        label="Anime.Quest",
        icon="github",
        url="https://github.com/MYTE21/Anime.Quest"
    )

with kaggle_column:
    mention(
        label="Anime Quest Dataset",
        icon="🎲",
        url="https://www.kaggle.com/datasets/myte21/anime-quest-an-epic-adventure-through-anime-data"
    )

with tableau_column:
    mention(
        label="Anime Quest: Visualization",
        icon="🎴",
        url="https://public.tableau.com/views/AnimeQuestVisualization/AnimeGeneralIdea?:language=en-US&:display_count=n&:origin=viz_share_link"
    )


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


def store_sessions():
    if "anime_compacted" not in st.session_state:
        st.toast("🧲 Getting Anime Compacted Data ..!")
        st.session_state["anime_compacted"] = get_anime_compacted_df()

    if "anime_country" not in st.session_state:
        st.toast("🧲 Getting Anime Compacted Data ..!")
        st.session_state["anime_country"] = get_anime_country_df()

    if "anime_watch" not in st.session_state:
        st.toast("🧲 Getting Anime Compacted Data ..!")
        st.session_state["anime_watch"] = get_anime_watch_df()


with st.spinner("💫 Collecting Data ..."):
    store_sessions()
    st.toast("🎉 Data Collection Completed..!")
