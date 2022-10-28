import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import datetime

def get_soup(url):
    r = requests.get(url)
    if r.status_code == 200:
        return BeautifulSoup(r.text,"html5lib")
    return None    

def get_news(item):
    data = {}
    heading = item.find("h2",class_="newsHdng")
    source=item.find("span",class_="posted-by")
    content=item.find("p",class_="newsCont")
    if heading is not None:
        data["heading"] = heading.text.strip()
    if source is not None:
        data["source"]  = source.text.strip()
    if content is not None:
        data["content"] = content.text.strip()
    return data    

def get_news_list(soup):
    headlines = []
    news = soup.find("div",class_="lisingNews")
    for item in news.find_all("div",class_="news_Itm"):
        headlines.append(get_news(item))
    return headlines

def main(filename="latest_news.csv"):
    pos = 1
    base_url = "https://www.ndtv.com/latest" 
    all_headlines = []
    while True:
        url =f"{base_url}/page-{pos}"
        print("➡",url)
        soup = get_soup(url)
        if soup is None:
            break
        else:
            headlines = get_news_list(soup)
            if headlines:
                all_headlines.extend(headlines)
            pos += 1
    #save
    if len(all_headlines)>0:
      time = datetime.datetime.now().strftime("%Y_%m_%d_%H")
      filename=f"{time}_{filename}"
      pd.DataFrame(all_headlines).to_csv(filename, index = False)        
        


if __name__ == "_main_" :
    main()               
