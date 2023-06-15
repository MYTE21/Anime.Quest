from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
import time


columns = ["Name", "Media Type", "Episodes", "Studio", "Start Year", "End Year", "Ongoing", "Release Season", "Rating",
           "Rank", "Members", "Genre", "Creator"]


def anime_details(anime_url):
    driver = webdriver.Chrome()
    driver.get(anime_url)

    name = driver.find_element(By.TAG_NAME, "h1").text.strip()

    media_info = driver.find_elements(By.CLASS_NAME, "pure-g")[1].text.split("\n")
    media_type = media_info[0].split("(")[0].strip()
    episodes_string = media_info[0].split("(")[1].strip(" ()")
    episodes = re.findall(r"\d+", episodes_string)[0]
    studio = [studio_name.strip() for studio_name in media_info[1].split(",")]

    if len(media_info[2].split("-")) == 2:
        start_year = media_info[2].split("-")[0].strip()
        end_year = media_info[2].split("-")[1].strip()
        end_year = end_year if end_year != "?" else None
        ongoing = True if end_year is None else False
    else:
        start_year = media_info[2].strip()
        end_year = None
        ongoing = False

    if len(media_info) == 6:
        release_season = media_info[3].split(" ")[0].strip()
        rating = media_info[4].split(" ")[0].strip()
        rank = media_info[5].split("#")[1].strip()
    else:
        release_season = None
        rating = media_info[3].split(" ")[0].strip()
        rank = media_info[4].split("#")[1].strip()

    members = driver.find_element(By.CLASS_NAME, "sidebarStats").text.split("\n")[1].split(" ")[0].replace(",", "")

    genre_class = driver.find_element(By.CLASS_NAME, "tags")
    genre_items = genre_class.find_elements(By.TAG_NAME, "li")
    genre = [genre_item.text.strip() for genre_item in genre_items]
    creator = driver.find_elements(By.CLASS_NAME, "CharacterCard__title")[8].text.strip()

    anime_contents = {"Name": name,
                      "Media Type": media_type,
                      "Episodes": episodes,
                      "Studio": studio,
                      "Start Year": start_year,
                      "End Year": end_year,
                      "Ongoing": ongoing,
                      "Release Season": release_season,
                      "Rating": rating,
                      "Rank": rank,
                      "Members": members,
                      "Genre": genre,
                      "Creator": creator}
    driver.close()

    return anime_contents


def get_all_anime():
    anime_data = []
    driver = webdriver.Chrome()

    start_page, end_page = 1, 654

    for page_id in range(start_page, end_page):
        url = f"https://www.anime-planet.com/anime/all?page={page_id}"
        driver.get(url)

        anime_links = driver.find_elements(By.CLASS_NAME, "tooltip")

        for idx, row in enumerate(anime_links[2:]):
            anime_link = row.get_attribute("href")
            anime_content = anime_details(anime_link)
            anime_data.append(anime_content)

        print(f"Collection in page {page_id}: {len(anime_links[2:])}")
        print(f"Collection in total: {len(anime_data)}\n")

    driver.close()
    anime_data_save(anime_data)


def anime_data_save(anime_data):
    if not os.path.isfile("../data/raw_data/anime_data.csv"):
        df = pd.DataFrame(data=anime_data, columns=columns)
        df.to_csv("../data/raw_data/anime_data.csv", index=False)
        print(f"Anime data saved as 'anime_data.csv' in '../data/raw_data/' folder..!")
    else:
        print(f"Not creating a new file.. Already exists anime data as 'anime_data.csv' in "
              f"'../data/raw_data/' folder..!")


def anime_scraping_main():
    start_time = time.time()

    print("Starting........")
    time.sleep(2)
    print("Scraping........!")
    # Get all the anime data
    get_all_anime()

    end_time = time.time()

    running_time = end_time - start_time
    minutes = (running_time / 60)
    print("Running time (in minutes): {:.2f}".format(minutes))


if __name__ == "__main__":
    anime_scraping_main()
