"""
Web scrapes Oscars movie titles and information from Rotten Tomatoes to collect raw movie data.
'movies.csv' will be created and put in the same directory.
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://editorial.rottentomatoes.com/guide/oscars-best-and-worst-best-pictures/"

response = requests.get(url)
if response.status_code != 200:
        raise Exception("URL could not be accessed")

soup = BeautifulSoup(response.text, "html.parser")
l = []

for i in range(1, 97):
    title_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-title-bar > div.col-sm-20.col-full-xs > div > div > h2 > a"
    title = soup.css.select(title_select)[0].text.strip()

    year_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-title-bar > div.col-sm-20.col-full-xs > div > div > h2 > span.subtle.start-year"
    year = soup.css.select(year_select)[0].text.strip()

    tomato_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-title-bar > div.col-sm-20.col-full-xs > div > div > h2 > span.tMeterScore"
    tomato = soup.css.select(tomato_select)[0].text.strip()

    consensus_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-details > div > div.info.critics-consensus"
    consensus = soup.css.select(consensus_select)[0].text.strip()

    synopsis_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-details > div > div.info.synopsis"
    synopsis = soup.css.select(synopsis_select)[0].text.strip()

    cast_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-details > div > div.info.cast"
    cast = soup.css.select(cast_select)[0].text.strip()

    director_select = f"#row-index-{i} > div.col-sm-18.col-full-xs.countdown-item-content > div.row.countdown-item-details > div > div.info.director > a"
    director = soup.css.select(director_select)[0].text.strip()

    data = {}
    data["Title"] = title
    data["Year"] = year
    data["Rotten Tomatoes Score"] = tomato
    data["Critic Consensus"] = consensus
    data["Synopsis"] = synopsis
    data["Cast"] = cast
    data["Director"] = director
    l.append(data)

df = pd.DataFrame(l)
df.to_csv('movies.csv', index=False, header=True)

print("Success! 'movies.csv' created in same directory.")