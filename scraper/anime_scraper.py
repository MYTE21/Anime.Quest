from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import pandas as pd
import os
import time


columns = ["Name", "Media Type", "Episodes", "Studio", "Start Year", "End Year", "Ongoing", "Release Season", "Rating",
           "Rank", "Members", "Genre", "Creator"]


def get_media_info(driver):
    media_section = driver.find_elements(By.CLASS_NAME, "pure-g")[1]
    media_infos = media_section.find_elements(By.CLASS_NAME, "pure-1")
    return [media_info.text for media_info in media_infos]


def get_media_type_episodes(media_info):
    media_type_episode = media_info[0].split("(")
    if len(media_type_episode) == 2:
        media_type = media_type_episode[0].strip()
        episodes_string = media_type_episode[1].strip(" ()")
        episodes = re.findall(r"\d+", episodes_string)[0]
    else:
        media_type = media_type_episode[0].strip()
        episodes = None

    return media_type, episodes


def get_media_year_season(media_info):
    media_year_season = media_info[2].split("\n")
    if len(media_year_season) == 2:
        media_year = media_year_season[0]
        season = media_year_season[1].split(" ")[0].strip()
    else:
        media_year = media_year_season[0]
        season = None

    if len(media_year.split("-")) == 2:
        start_year = media_year.split("-")[0].strip()
        end_year = media_year.split("-")[1].strip()
        end_year = end_year if end_year != "?" else None
        ongoing = True if end_year is None else False
    else:
        start_year = None if media_year.strip() == "TBA" else media_year.strip()
        end_year = None
        ongoing = False

    return start_year, end_year, ongoing, season


def get_creator_id(person_profession, text):
    for i, person in enumerate(person_profession):
        if text in person:
            return i

    return -1


def get_creator(driver):
    person_profession = [x.text for x in driver.find_elements(By.CLASS_NAME, "CharacterCard__body")]
    person_name = [x.text for x in driver.find_elements(By.CLASS_NAME, "CharacterCard__title")]

    creator_index = get_creator_id(person_profession, "Original Creator")
    director_index = get_creator_id(person_profession, "Director")

    if creator_index != -1:
        creator = person_name[creator_index]
    elif director_index != -1:
        creator = person_name[director_index]
    else:
        creator = None

    return creator


def anime_details(anime_url):
    driver = webdriver.Chrome()
    driver.get(anime_url)

    name = driver.find_element(By.TAG_NAME, "h1").text.strip()

    media_info = get_media_info(driver)

    media_type, episodes = get_media_type_episodes(media_info)
    studio = [studio_name.strip() for studio_name in media_info[1].split(",")]
    start_year, end_year, ongoing, release_season = get_media_year_season(media_info)

    rating_data = media_info[3].split(" ")[0].strip()
    rating = None if rating_data == "" else rating_data

    rank_data = media_info[4].split("#")
    rank = None if len(rank_data) == 1 else rank_data[1].strip()

    members = driver.find_element(By.CLASS_NAME, "sidebarStats").text.split("\n")[1].split(" ")[0].replace(",", "")

    try:
        genre_class = driver.find_element(By.CLASS_NAME, "tags")
        genre_items = genre_class.find_elements(By.TAG_NAME, "li")
        genre = [genre_item.text.strip() for genre_item in genre_items]
    except Exception as e:
        genre = []

    creator = get_creator(driver)

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
        print("\n #PAGE: ", page_id, "\n", "=" * 120)

        for idx, row in enumerate(anime_links[2:]):
            anime_link = row.get_attribute("href")
            print(f"({idx}) Running ... {anime_link}")
            anime_content = anime_details(anime_link)
            anime_data.append(anime_content)

        print(f"\nCollection in page {page_id}: {len(anime_links[2:])}")
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
