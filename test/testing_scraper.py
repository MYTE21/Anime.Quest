from selenium import webdriver
from selenium.webdriver.common.by import By
import re
from scraper.anime_scraper import anime_details


def test_anime_details(anime_url):
    driver = webdriver.Chrome()
    driver.get(anime_url)

    name = driver.find_element(By.TAG_NAME, "h1").text.strip()

    media_section = driver.find_elements(By.CLASS_NAME, "pure-g")[1]
    media_infos = media_section.find_elements(By.CLASS_NAME, "pure-1")
    media_info = [x.text for x in media_infos]
    print(media_info)

    # ! media type + episodes
    media_type_episode = media_info[0].split("(")
    if len(media_type_episode) == 2:
        media_type = media_type_episode[0].strip()
        episodes_string = media_type_episode[1].strip(" ()")
        episodes = re.findall(r"\d+", episodes_string)[0]
    else:
        media_type = media_type_episode[0].strip()
        episodes = None

    # print("media_type: ", media_type)
    # print("episodes: ", episodes)

    # ! studio
    studio = [studio_name.strip() for studio_name in media_info[1].split(",")]
    # print("studio: ", studio)

    # ! start_year, end_year, ongoing, release_season
    media_year_season = media_info[2].split("\n")
    if len(media_year_season) == 2:
        media_year = media_year_season[0]
        season = media_year_season[1].split(" ")[0].strip()
    else:
        media_year = media_year_season[0]
        season = None
    # print("media_year: ", media_year)
    # print("season: ", season)

    if len(media_year.split("-")) == 2:
        start_year = media_year.split("-")[0].strip()
        end_year = media_year.split("-")[1].strip()
        end_year = end_year if end_year != "?" else None
        ongoing = True if end_year is None else False
    else:
        start_year = None if media_year.strip() == "TBA" else media_year.strip()
        end_year = None
        ongoing = False

    # print("start_year: ", start_year)
    # print("end_year: ", end_year)
    # print("ongoing: ", ongoing)

    # ! rating
    rating_data = media_info[3].split(" ")[0].strip()
    rating = None if rating_data == "" else rating_data
    # print("rating: ", rating)

    # ! rank
    rank_data = media_info[4].split("#")
    rank = None if len(rank_data) == 1 else rank_data[1].strip()
    print("rank: ", rank)

    driver.close()


def test_creator_index(person_profession, text):
    for i, person in enumerate(person_profession):
        if text in person:
            return i

    return -1


def test_creator(anime_url):
    driver = webdriver.Chrome()
    driver.get(anime_url)

    name = driver.find_element(By.TAG_NAME, "h1").text.strip()

    person_profession = [x.text for x in driver.find_elements(By.CLASS_NAME, "CharacterCard__body")]
    person_name = [x.text for x in driver.find_elements(By.CLASS_NAME, "CharacterCard__title")]

    creator_index = test_creator_index(person_profession, "Original Creator")
    director_index = test_creator_index(person_profession, "Director")

    if creator_index != -1:
        creator = person_name[creator_index]
    elif director_index != -1:
        creator = person_name[director_index]
    else:
        creator = None

    driver.close()

    print("name: ", name)
    print("creator: ", creator)
    print("-" * 30)


if __name__ == "__main__":
    urls = [
        "https://www.anime-planet.com/anime/fullmetal-alchemist-brotherhood",
        "https://www.anime-planet.com/anime/fruits-basket-the-final-season",
        "https://www.anime-planet.com/anime/bleach-thousand-year-blood-war",
        "https://www.anime-planet.com/anime/attack-on-titan-the-final-season-the-final-chapters",
        "https://www.anime-planet.com/anime/yawaraka-atom",
        "https://www.anime-planet.com/anime/eggroy",
        "https://www.anime-planet.com/anime/hizukuri"
    ]

    for idx, url in enumerate(urls):
        print(f"({idx + 1})")
        test_creator(url)
