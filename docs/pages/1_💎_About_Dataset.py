import streamlit as st
from streamlit_extras.app_logo import add_logo
from PIL import Image


st.set_page_config(
        page_title="About Dataset | Anime Quest",
        page_icon="docs/icons/anime_quest_icon.png",
        menu_items={
            'About': "This is about section..!",
            'Report a bug': "https://github.com/MYTE21/Anime.Quest/issues/new",
        }
)

st.header("Anime Quest Dataset")
add_logo("docs/icons/anime_quest_icon.png", height=3)

st.caption("From Classics to Hidden Gems: Anime data about 22,888 anime entries")

"""
[Anime Quest Dataset](https://www.kaggle.com/datasets/myte21/anime-quest-an-epic-adventure-through-anime-data) 
contains information about [Anime](https://en.wikipedia.org/wiki/Anime) scraped from 
[Anime Planet](https://www.anime-planet.com/) on `28/06/2023`. It contains information about anime 
(episodes, aired date, rating, genre, etc.), and favorite anime based on the countries and top countries 
that watch the most anime.
"""

image = Image.open("assets/anime_data.png")
st.image(image)

anime_compacted_tab, anime_country_tab, anime_watch_tab = st.tabs(["Anime Details",
                                                                   "Anime & Country",
                                                                   "Anime & Watch Count"])

with anime_compacted_tab:
    """
    The `anime_data.csv` file is scraped from the [🌐Anime Planet](https://anime-planet.com/) website. 
    This file contains a total of **22,888** anime details in **13 columns**.
    """

with anime_country_tab:
    """
    The `anime_top_by_country_data.csv` file is downloaded from the 
    [🌐Every Country’s Favorite Anime](https://e.infogram.com/f2bfaed8-7046-43e6-aa41-367848a326ef?parent_url=https%3A%2F%2Fwww.broadbandchoices.co.uk%2Ffeatures%2Fevery-countrys-favourite-anime&src=embed#) 
    website. It contains the top **5 favorite anime of all the countries** in the world.
    """

with anime_watch_tab:
    """
    The `anime_watching_data.csv` file is scraped from the 
    [🌐List of Countries that Watch the Most Anime](https://skdesu.com/en/list-of-countries-that-watch-the-most-anime/) 
    website.
    """