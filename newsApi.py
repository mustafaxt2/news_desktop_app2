import requests

class NewsApi:
    businessNews=[]
    entertainmentNews=[]
    sportsNews=[]
    scienceNews=[]
    healthNews=[]
    technologyNews=[]

    def __init__(self) -> None:
        self._url="https://newsapi.org/v2/top-headlines?"
        self._apiKey="96d4893062974f74ab84841ce82c5096"
        self._country="us"

    def get_news(self,category,liste):
        response=requests.get(self._url,params={"apiKey":self._apiKey, "country":self._country ,"category":category})
        news=response.json()["articles"]
        
        for new in news:
            liste.append(New(new["title"],new["url"]))
        return liste
        
news=NewsApi()

class New:
    def __init__(self,title,url) -> None:
        self._title=title
        self._url=url