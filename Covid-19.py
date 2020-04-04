from bs4 import BeautifulSoup
import requests
import time
from time import gmtime, strftime, localtime
import curses
import sys

class parser():
    headers = {"User-Agent" : "Mozilla/5.0"}
    world = requests.get("https://www.worldometers.info/coronavirus/", headers = headers)
    united_states = requests.get("https://www.worldometers.info/coronavirus/country/us/", headers = headers)
    louisiana = requests.get("https://www.nola.com/news/coronavirus/article_7cb2af1c-6414-11ea-b729-93612370dd94.html", headers = headers)
    world_src = world.content
    united_states_src = united_states.content
    la_src = louisiana.content
    world_soup = BeautifulSoup(world_src, "html.parser")
    us_soup = BeautifulSoup(united_states_src, "html.parser")
    la_soup = BeautifulSoup(la_src, "html.parser")



def world_wide():
    print("\nWorld-Wide \n----------")
    url = parser.world_soup
    parent = url.find("div", {"class": "content-inner"})
    for div in parent.find_all("div", {"id": "maincounter-wrap"}):
        ww_title = div.find_all('h1')[0].text.strip()
        for ww_number in div.find("span"):
            print(ww_title, ww_number)



def usa():
    print("\nUnited States \n-------------")
    count = 0
    category1 = ""
    category2 = ""
    category3 = ""
    url = parser.us_soup
    parent = url.find("div", {"class": "content-inner"})
    for div in parent.find_all("div",{"id": "maincounter-wrap"}):
        for h1 in div.find_all("h1"):
            us_category = h1.text.strip()
            count+=1
            if count == 1:
                category1 = us_category
            elif count == 2:
                category2 = us_category
            elif count == 3:
                category3 = us_category
    #Scrapes the number associated with each category
    count = 0
    num1 = 0
    num2 = 0
    num3 = 0
    for div in parent.find_all("div", {"class": "maincounter-number"}):
        for span in div.find_all("span"):
            us_num = span.text.strip()
            count += 1
            if count == 1:
                num1 = us_num
            elif count == 2:
                num2 = us_num
            elif count == 3:
                num3 = us_num
    print(category1, num1)
    print(category2, num2)
    print(category3, num3)



def louisiana():
    print("\nLouisiana \n---------")
    count = 0
    num1 = 0
    num2 = 0
    num3 = 0
    url = parser.la_soup
    for div in url.find_all("div", {"class": "row"}):
        for div2 in div.find_all("div",{"class": "col-md-offset-1 col-md-10"}):
            for div3 in div2.find_all("div",{"class": "asset-content subscriber-premium"}):
                for h1 in div3.find("h1"):
                    la_total_cases = h1.text.strip()
                    print("Coronavirus Cases: "+la_total_cases)
                for h1 in div3.find_all("h1"):
                    h1 = h1.text.strip()
                    count += 1
                    if count == 1:
                        num1 = h1
                    elif count == 2:
                        num2 = h1
                    elif count == 3:
                        num3 = h1
            print("Deaths: "+num2)




def main():
    while True:
        sys.stdout.flush()
        current_time = strftime("%a, %b %d %Y %H:%M:%S", localtime())
        print("COVID-19 OUTBREAK -- "+ current_time+"\n", end="\r", flush=True)
        sys.stdout.flush()
        world_wide()
        usa()
        louisiana()
        time.sleep(100)


main()
