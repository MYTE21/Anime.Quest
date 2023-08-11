import streamlit as st
from PIL import Image

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

from utilities.database import get_anime_compacted_df, get_anime_country_df, get_anime_watch_df


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


st.write("General Idea Page..!")
st.write("Anime Compacted Shape: ", get_anime_compacted_df().shape)
st.write("Anime Country Shape: ", get_anime_country_df().shape)
st.write("Anime Watch Shape: ", get_anime_watch_df().shape)
