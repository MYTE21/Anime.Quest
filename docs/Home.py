import streamlit as st
from PIL import Image

from streamlit_extras.app_logo import add_logo
from streamlit_extras.mention import mention
from streamlit_card import card
import base64


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
st.caption("Data collection and analysis to discover fascinating information about anime")
st.info("🛠️ Under Development")
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

# Card Generate for github, kaggle and tableau
def card_generate(file_path, title, text, url):
    with open(file_path, "rb") as file:
        data = file.read()
        encoded = base64.b64encode(data)

    data = "data:image/png;base64," + encoded.decode("utf-8")

    card(
        title=title,
        text=text,
        image=data,
        url=url,
        on_click=lambda: None,
        styles={
            "card": {
                "width": "180px",
                "height": "150px",
                "margin": "0px"
            },
            "text": {
                "font-size": "15px"
            }
        }
    )


github_column, kaggle_column, tableau_column = st.columns(3)
with github_column:
    card_generate("docs/icons/github_icon.png", "Anime.Quest", "GitHub Source Code", "https://github.com/MYTE21/Anime.Quest")

with kaggle_column:
    card_generate("docs/icons/kaggle_icon.png", "Anime Quest Dataset", "Scraped Data", "https://www.kaggle.com/datasets/myte21/anime-quest-an-epic-adventure-through-anime-data")

with tableau_column:
    card_generate("docs/icons/tableau_icon.png", "Anime Quest: Visualization", "Data Visualization", "https://public.tableau.com/app/profile/myte/viz/AnimeQuestVisualization/AnimeGeneralIdea")



"""
### Project Goal
Giving the project a data analysis tag will help us classify it more broadly. But after breaking down the wider concept, we can extract the project's goal, which is as follows:

1. [Scraping](https://en.wikipedia.org/wiki/Web_scraping) a [dynamic website](https://en.wikipedia.org/wiki/Dynamic_web_page) to extract details about anime.
2. Improve the extracted data's usability by processing it. a.k.a. **Data Processing**.
3. Use [Tableau Public](https://public.tableau.com/app/discover) to visualize the dataset to obtain valuable anime-related information.

***Other aspect of the project:***

1. **Exploratory Data Analysis**: Analyzing the data thoroughly and utilizing visual means to learn various data characteristics.
2. **Automatic testing** of the scraper files.
3. Utilizing [Streamlit](https://streamlit.io/), create an experiment and data-driven web application.
"""

"""
### Resources and Websites
1. `Anime details` are collected using scraping from the [Anime Planet](https://www.anime-planet.com/) website.
2. Information about `anime countries` is gathered from the [Every Country's Favourite Anime](https://e.infogram.com/f2bfaed8-7046-43e6-aa41-367848a326ef?parent_url=https%3A%2F%2Fwww.broadbandchoices.co.uk%2Ffeatures%2Fevery-countrys-favourite-anime&src=embed#) website.
3. Data of `countries that watch the most anime` are collected using scraping from the [List of Countries that Watch the Most Anime](https://skdesu.com/en/list-of-countries-that-watch-the-most-anime/) website.
"""

"""
### Contributors
**Project Owner**
"""

owner_image, owner_name, owner_linkedin = st.columns(3)

with owner_image:
    st.image("assets/md_yasmi_tohabar.jpg", width=50)

with owner_name:
    st.write("Md Yasmi Tohabar")

with owner_linkedin:
    """
    [www.linkedin.com/in/myte/](https://www.linkedin.com/in/myte/)
    """

"""
### License

The [Anime Quest](https://github.com/MYTE21/IC.Photography.Styles) project is released under the [MIT License](https://github.com/MYTE21/Anime.Quest/blob/main/LICENSE).
Feel free to use, modify, and distribute the project in accordance with the license terms.

### Contact

For any inquiries or questions regarding the [Anime Quest](https://github.com/MYTE21/IC.Photography.Styles) project,
please contact at [yasmi.tohabar@gmail.com](mailto:yasmi.tohabar@gmail.com).
We appreciate your interest and feedback.
"""