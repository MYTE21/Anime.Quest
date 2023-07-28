from dummy_data.given_data import urls
from dummy_data.expected_data import anime_info
from scrapers.anime_scraper import anime_details


def test_anime_details():
    for i, url in enumerate(urls):
        ad = anime_details(url)
        assert ad["Name"] == anime_info[i]["Name"]
        assert ad["Media Type"] == anime_info[i]["Media Type"]
        assert ad["Episodes"] == anime_info[i]["Episodes"]
        assert ad["Studio"] == anime_info[i]["Studio"]
        assert ad["Start Year"] == anime_info[i]["Start Year"]
        assert ad["End Year"] == anime_info[i]["End Year"]
        assert ad["Ongoing"] == anime_info[i]["Ongoing"]
        assert ad["Release Season"] == anime_info[i]["Release Season"]
        assert ad["Genre"] == anime_info[i]["Genre"]
        assert ad["Creator"] == anime_info[i]["Creator"]
