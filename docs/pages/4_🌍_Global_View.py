import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(
        page_title="Global View | Anime Quest",
        page_icon="docs/icons/anime_quest_icon.png",
        menu_items={
            'About': "This is about section..!",
            'Report a bug': "https://github.com/MYTE21/Anime.Quest/issues/new",
        }
)

from utilities.database import get_anime_compacted_df, get_anime_country_df, get_anime_watch_df

st.header("Global View")
add_logo("docs/icons/anime_quest_icon.png", height=3)

st.write("Global View Page..!")
st.write("Anime Compacted Shape: ", get_anime_compacted_df().shape)
st.write("Anime Country Shape: ", get_anime_country_df().shape)
st.write("Anime Watch Shape: ", get_anime_watch_df().shape)