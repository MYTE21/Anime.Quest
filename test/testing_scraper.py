from selenium import webdriver
from selenium.webdriver.common.by import By
import re


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

    person_profession = [x.text for x in driver.find_elements(By.CLASS_NAME, "CharacterCard__body")]
    person_name = [x.text for x in driver.find_elements(By.CLASS_NAME, "CharacterCard__title")]
    try:
        # TODO: If person_profession contains 'Original Creator' partially that should be acceptable
        creator_id = person_profession.index("Original Creator")
        creator = person_name[creator_id]
    except ValueError:
        creator = None

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


if __name__ == "__main__":
    urls = [
        "https://www.anime-planet.com/anime/attack-on-titan-the-final-season-the-final-chapters",
        "https://www.anime-planet.com/anime/eggroy",
        "https://www.anime-planet.com/anime/yawaraka-atom"
        "https://www.anime-planet.com/anime/hizukuri"
    ]

    for url in urls:
        details = anime_details(url)
        print(details)
