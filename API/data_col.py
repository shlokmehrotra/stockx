import requests
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen


def price(company):
    url = "https://finance.yahoo.com/quote/" + company + "?p=" + company + "&.tsrc=fin-srch"
    page = urlopen(url)

    soup = bs4.BeautifulSoup(page,"html.parser")
    try: 
        price = soup.find("div",{"class": "My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").text
    except: 
        return -1
    print("price found for: " + str(company))
    return price
