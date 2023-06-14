from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


columns = ["Name", "Media Type", "Episodes", "Studio", "Start Year", "End Year", "Ongoing", "Release Season", "Rating",
           "Rank", "Members", "Genre", "Creator"]


def anime_details():
    pass


def get_all_anime():
    start_page, end_page = 1, 5
    anime_list = []
    for page_id in range(start_page, end_page):
        url = f"https://www.anime-planet.com/anime/all?page={page_id}"

        driver = webdriver.Chrome()
        driver.get(url)

        anime_names = driver.find_elements(By.CLASS_NAME, "cardName")

        for idx, row in enumerate(anime_names):
            anime_name = row.text
            anime_list.append(anime_name)

        driver.close()

    print(len(anime_list))


if __name__ == "__main__":
    get_all_anime()
