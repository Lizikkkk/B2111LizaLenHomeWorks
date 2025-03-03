import sqlite3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup.list = soup.find_all("day", {"data-pattern": "G:i"})
    res1 = soup.list[0]
    soup.list2 = soup.find_all("temperature-value", {"from-unit": "c"})
    res2 = soup.list2[0]

conection = sqlite3.connect("itstep_DB.sl3", 5)
cur = conection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES (res1), (res2);")
conection.commit()
conection.close()







