from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os


columns = ["Rank", "Country", "Population", "Percentage of People Watching", "Number of People Watching"]


def anime_watch_data():
    anime_url = "https://skdesu.com/en/list-of-countries-that-watch-the-most-anime/"

    driver = webdriver.Chrome()
    driver.get(anime_url)

    rank_rows = driver.find_elements(By.TAG_NAME, "td")
    rank, country, population, percentage_watching, people_watching = [], [], [], [], []

    for idx, rank_row in enumerate(rank_rows[5:]):
        if idx % 5 == 0:
            rank.append(rank_row.text)
        elif idx % 5 == 1:
            country.append(rank_row.text)
        elif idx % 5 == 2:
            population.append(rank_row.text.replace(",", ""))
        elif idx % 5 == 3:
            percentage_watching.append(rank_row.text.replace("%", ""))
        else:
            people_watching.append(rank_row.text.replace(",", ""))

    driver.close()

    anime_watching_contents = []
    for i in range(10):
        anime_watching_content = {"Rank": rank[i],
                                  "Country": country[i],
                                  "Population": population[i],
                                  "Percentage of People Watching": percentage_watching[i],
                                  "Number of People Watching": people_watching[i]}
        anime_watching_contents.append(anime_watching_content)

    return anime_watching_contents


def anime_watch_data_save():
    awd = anime_watch_data()
    path = os.path.join("./data/raw_data", "anime_watch_data.csv")

    if not os.path.isfile(path):
        df = pd.DataFrame(data=awd, columns=columns)
        df.to_csv(path, index=False)
        print(f"Anime Watch data saved as 'anime_watch_data.csv' in './data/raw_data/' folder..!")
        return df.shape[0]
    else:
        print("File already exists ..!")


if __name__ == "__main__":
    anime_watch_data_save()
