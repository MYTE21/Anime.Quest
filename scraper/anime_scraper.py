from selenium import webdriver
from selenium.webdriver.common.by import By
import re


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
    else:
        start_year = media_info[2].strip()
        end_year = None
    ongoing = True if end_year is None else False

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
    driver = webdriver.Chrome()

    start_page, end_page = 1, 2

    for page_id in range(start_page, end_page):
        url = f"https://www.anime-planet.com/anime/all?page={page_id}"
        driver.get(url)

        anime_links = driver.find_elements(By.CLASS_NAME, "tooltip")

        for idx, row in enumerate(anime_links[2:]):
            anime_link = row.get_attribute("href")
            print("<", "-" * 20, ">")
            print(f"({idx}) ", anime_link)
            anime_content = anime_details(anime_link)
            print(anime_content)
            print("<", "-" * 20, ">")
            if idx == 3:
                break

    driver.close()


if __name__ == "__main__":
    get_all_anime()
