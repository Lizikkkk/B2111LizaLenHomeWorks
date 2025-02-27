from bs4 import BeautifulSoup
import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup.list = soup.find_all("td", {"data-label": "Офіційний курс"})
    res = soup.list[7]

grn = float(input("Напишіть скільки у вас грошей "))
dol = grn/float(res.text.replace(',', '.'))
print(f"{grn} грн - це {dol} долларів")