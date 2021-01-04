from bs4 import BeautifulSoup as bs
import requests
from .models import Url, ParsingInfo
from .views import *
import json


class Parser:
    #url = Url.objects.all()
    """def __init__(self, url):
        self.url = url
        r = requests.get(url)
        if r.status_code != 200:
            print("Cannot get destination, status code is: {0}".format(r.status_code))"""

    def get_title(self, url):
        self.url = url
        r = requests.get(url)
        html_src = r.text
        page = bs(html_src, "lxml")
        get_tittle = page.findAll("title")
        get_heading = page.findAll("h1")
        title = []
        title.append(r.encoding)
        for item in get_tittle:
            title.append(item.string)
        for item_1 in get_heading:
            title.append(item_1.string)
        title = json.dumps(title, ensure_ascii=False)
        return ParsingInfo.objects.create(content=title)

    def parse_urls(self):
        url = list(Url.objects.all())
        for i in url:
            self.get_title(i)
        return
