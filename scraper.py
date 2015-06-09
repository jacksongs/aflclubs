# This scraper collects all the AFL players from each of the club websites

import scraperwiki
import requests
from bs4 import BeautifulSoup

afl = requests.get("http://www.afl.com.au")

aflsoup = BeautifulSoup(afl.content)

aflul = aflsoup.find("ul", class_="team-logos")
afllis = aflul.find_all("li")

teams = {}
players = {}
data = []
for i, a in enumerate(afllis):
	data.append({"id": i, "name": a.a.text, "link": a.a.get("href")})
	
scraperwiki.sqlite.save(unique_keys=["name"], data=data, table_name='clubs')
