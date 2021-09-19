"""
### Please note: This file is not for execution ###
"""

import requests
import json

"""
ReadJson.py
"""
response = requests.get("http://data.ntpc.gov.tw/api/v1/rest/datastore/382000000A-000352-001")
content = response.content
json_tree = json.loads(content)

for bike_rent_records in json_tree["result"]["records"]:
    leftRatio = float(bike_rent_records["sbi"]) / float(bike_rent_records["tot"]) * 100
    print("ID:{0} Left:{2:%0.1f} Name:{1}".format(bike_rent_records["sno"], bike_rent_records["aren"], leftRatio))

"""
ReadRSS.py
"""

import feedparser

# retrieve RSS feedback
content = feedparser.parse("https://www.ft.com/?edition=international&format=rss")

contentWSJ = feedparser.parse("http://www.wsj.com/public/page/rss_news_and_feeds.html")

# list all titles
print("\nTitles-------------------------\n")
for index, item in enumerate(content.entries):
    print("{0}.{1}".format(index, item["title"]))

# list all description
print("\r\nDescriptions-------------------\r\n")
for index, item in enumerate(content.entries):
    print("{0}.{1}\n".format(index, item["description"]))

"""
NASDAQ_headlines_1stpage.py
"""

import requests
from bs4 import BeautifulSoup as soup
import datetime
import pandas as pd
import os
import pickle

# Using the requests module to get source code from the url
nasdaq_url = 'https://www.nasdaq.com/news-and-insights/topic/markets/stocks/page/1'

direct = os.getcwd() + '/DEDA_WebScrapingIntro/'
# Or:
# direct = os.getcwd()

refresh = True

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Upgrade-Insecure-Requests": "1", "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
# Header is used to deceive the webpage host server that we are visiting the webpage via a browser

if (not os.path.exists(direct + 'temp/' + '0.pkl')) or (refresh is True):
    # connect to the website if the webpage source code file is not exist or we need to refresh it
    url_request = requests.get(nasdaq_url, headers=headers)
    status_code = url_request.status_code

    if status_code != 200:
        raise ConnectionRefusedError("Unable to connect to the website")
    # save the request object after scraping
    with open(direct + 'temp/' + '0.pkl', 'wb') as url_file:
        pickle.dump(url_request, url_file)
else:
    # else, we open the source code file from local disk to save time
    with open(direct + 'temp/' + '0.pkl', 'rb') as url_file:
        url_request = pickle.load(url_file)

url_content = url_request.content
# Using BeautifulSoup to parse webpage source code
parsed_content = soup(url_content, "html.parser")

# Using .find_all() method to search tag name and attribute
containers = parsed_content.find_all('div', {'data-type': 'article'})
page_info = list()  # initial empty list to load the data

for container in containers:
    """
    Scrape 1 item each time, each item contains title, time, author_name, tag, author_url 
    """
    unit_info = dict()

    # Find title item
    container_title = container.find_all('a', {"class": "content-feed__card-title-link"})

    if container_title == []:
        continue

    news_link = container_title[0].get('href').strip()
    news_link = f"https://www.nasdaq.com{news_link}"
    news_title = container_title[0].text.strip()  # strip() method can remove specific chars at the head and tail
    unit_info['news_title'] = news_title
    unit_info['news_link'] = news_link

    try:
        # Using try...except to catch unexpected condition so that program can keep running
        # Formatting date see further more: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

        news_date = datetime.datetime.strptime(news_link[-10:], '%Y-%m-%d')
        news_date = news_date.date()

    except:
        container_time = container.find_all('div', {'class': 'content-feed__card-timestamp'})
        try:
            news_date = datetime.datetime.strptime(container_time[0].text.strip(), '%b %d,%Y')
            news_date = news_date.date()

        except:
            t_day = datetime.date.today()
            date_series = container_time[0].text.strip().split(' ')
            if (date_series[1].startswith('hour')) or (date_series[1].startswith('minute')):
                news_date = t_day

            elif date_series[1].startswith('day'):
                news_date = t_day - datetime.timedelta(days=int(date_series[0]))
            else:
                news_date = t_day

    news_date = datetime.datetime(news_date.year, news_date.month, news_date.day)
    unit_info['news_time'] = news_date
    page_info.append(unit_info)

nasdaq_info_df = pd.DataFrame(page_info, columns=['news_title', 'news_link', 'news_time'])
nasdaq_info_df.to_csv(direct + '/Nasdaq_headline_onepage.csv')

"""
NasdaqNewsScraping_Function.py
"""

from bs4 import BeautifulSoup as soup
import requests
import datetime
import os
import pandas as pd
import pickle

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    "Upgrade-Insecure-Requests": "1", "DNT": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
# Header is used to deceive the webpage host server that we are visiting the webpage via a browser

def nasdaq_news_scraping(page=1, refresh=False):
    # Argument page equals 1 by default
    nasdaq_url = f'https://www.nasdaq.com/news-and-insights/topic/markets/stocks/page/{page}'

    if (not os.path.exists(direct + '/temp/' + str(page) + '.pkl')) or (refresh is True):
        # connect to the website if the webpage source code file is not exist of we need to refresh it
        url_request = requests.get(nasdaq_url, headers=headers)
        # save the request object after scraping
        with open(direct + '/temp/' + str(page) + '.pkl', 'wb') as url_file:
            pickle.dump(url_request, url_file)
    else:
        # else, we open the source code file from local disk to save time
        with open(direct + '/temp/' + str(page) + '.pkl', 'rb') as url_file:
            url_request = pickle.load(url_file)
    url_content = url_request.content
    parsed_content = soup(url_content, "html.parser")
    containers = parsed_content.find_all('div', {'data-type': 'article'})
    page_info = list()

    for container in containers:
        """
        Scrape 1 item each time, each item contains title, time, author_name, tag, author_url 
        """
        unit_info = dict()

        container_title = container.find_all('a', {"class": "content-feed__card-title-link"})
        if container_title == []:
            continue

        news_link = container_title[0].get('href').strip()
        news_link = f"https://www.nasdaq.com{news_link}"
        news_title = container_title[0].text.strip()
        unit_info['news_title'] = news_title
        unit_info['news_link'] = news_link

        try:
            news_date = datetime.datetime.strptime(news_link[-10:], '%Y-%m-%d')
            news_date = news_date.date()

        except:
            container_time = container.find_all('div', {'class': 'content-feed__card-timestamp'})
            try:
                news_date = datetime.datetime.strptime(container_time[0].text.strip(), '%b %d,%Y')
                news_date = news_date.date()

            except:
                t_day = datetime.date.today()
                date_series = container_time[0].text.strip().split(' ')
                if (date_series[1].startswith('hour')) or (date_series[1].startswith('minute')):
                    news_date = t_day

                elif date_series[1].startswith('day'):
                    news_date = t_day - datetime.timedelta(days=int(date_series[0]))
                else:
                    news_date = t_day

        news_date = datetime.datetime(news_date.year, news_date.month, news_date.day)
        unit_info['news_time'] = news_date
        page_info.append(unit_info)

    return page_info


direct = os.getcwd() + '/DEDA_WebScrapingIntro/'
# Or
# direct = os.getcwd()

head_lines_info = list()

for page_num in range(1, 30):
    print("This is Page: ", page_num)
    # Using the function defined previously with certain arguments as input
    page_info = nasdaq_news_scraping(page=page_num, refresh=True)
    head_lines_info.extend(page_info)

headlines_info_df = pd.DataFrame(head_lines_info, columns=['news_title', 'news_link', 'news_time'])
headlines_info_df.to_csv(direct + '/Nasdaq_News_MultiPages.csv')

"""
ChinaCities_WeatherPageScraping.py
"""

"""
This is a preliminary tutorial for scraping web pages

"""

# Import all the packages you need, always remember that you can find 99% packages you need in python
import requests  # take the website source code back to you
import urllib  # some useful functions to deal with website URLs
from bs4 import BeautifulSoup as soup  # a package to parse website source code
import numpy as np  # all the numerical calculation related methods
import re  # regular expression package
import itertools  # a package to do iteration works
import pickle  # a package to save your file temporarily
import pandas as pd  # process structured data

save_path = 'output/'  # the path you save your files

base_link = 'http://www.tianqihoubao.com/lishi/'  # This link can represent the domain of a series of websites


def city_collection():
    request_result = requests.get(base_link)  # get source code
    parsed = soup(request_result.content)  # parse source code

    dt_items = parsed.find_all('dt')  # find the items with tag named 'dt'
    for item in dt_items:
        # iterate within all the items
        province_name = item.text.strip()  # get name of the province
        province_link2cities = item.find('a')['href']  # get link to all the cities in the province
        province = {'province_link': province_link2cities}
        provinces[province_name] = province  # save dict in the dict

    for province in provinces.keys():
        # iterate with the province link to find all the cities
        cities = {}
        print(provinces[province]['province_link'])
        request_province = requests.get(urllib.parse.urljoin(base_link, provinces[province]['province_link']))
        # use the urllib package to join relative links in the proper way
        parsed_province = soup(request_province.content)
        dd_items = parsed_province.find_all('dd')
        for dd_item in dd_items:
            print(dd_item)
            cities_items = dd_item.find_all('a')
            for city_item in cities_items:
                city_name = city_item.text.strip()
                city_link = city_item.get('href').split('.')[0]
                cities[city_name] = city_link
        provinces[province]['cities'] = cities
    return provinces


def weather_collection(link):
    """
    use the link to collect the weather data
    :param link: url link
    :return: dict, weather of a city everyday
    """
    weather_page_request = requests.get(link)
    parsed_page = soup(weather_page_request.content)
    tr_items = parsed_page.find_all('tr')
    month_weather = dict()
    for tr_item in tr_items[1:]:
        # print(tr_item)
        # daily_weather = dict()
        td_items = tr_item.find_all('td')
        date = td_items[0].text.strip()
        split_pattern = r'[\n\r\s]\s*'
        weather_states = ''.join(re.split(split_pattern, td_items[1].text.strip()))
        temperature = ''.join(re.split(split_pattern, td_items[2].text.strip()))
        wind = ''.join(re.split(split_pattern, td_items[3].text.strip()))
        month_weather[date] = {
            'weather': weather_states,
            'tempe': temperature,
            'wind': wind
        }
        # month_weather.append(daily_weather)
    return month_weather


# Nice way to get a date string with certain format
years = np.arange(start=2011, stop=2018)
months = np.arange(start=1, stop=13)
it = list(itertools.product(years, months))
date = [str(ele[0]) + format(ele[1], '02d') for ele in it]  # '02d' means 2 digits

#  ==== Since I have already download the links to all the cities, you just need to execute from here:=====
#  ==== Otherwise, use function below to retrieve provinces information ======
provinces = dict()  # initialize a dictionary to hold provinces information
# This dictionary includes 'province_link' which means links to find the cities for each province
# and the 'cities' which means city names and links
# provinces_info = city_collection()  # Use this function to retrieve links to all the cities

# This is called context management, with open can close the document automatically when the
with open('DEDA_Class_2017_WebScrapingIntro/output_cities_link.pkl', 'rb') as cities_file:  # write, change 'rb' -> 'wb'
    provinces_info = pickle.load(cities_file)
    print(provinces_info)
    # pickle.dump(provinces_info, cities_file)  # write

weather_record = dict()
# The structure is dict in dict
# first layer keyword is province name
# In each province you can find the cities
# In each city, you can find the date, in the date, you can find weather record
for key in provinces_info.keys():
    # Iterate over different provinces
    print(key)
    for city_name, city_link in provinces_info[key]['cities'].items():
        # Iterate cities within each provinces
        print(city_name)
        for month_date in date:
            # Iterate over different months
            print(city_name)
            print(month_date)
            print(provinces_info[key]['cities'][city_name])
            print("On Scraping...")
            month_weather = weather_collection(
                urllib.parse.urljoin(base_link, city_link) + '/month/' + month_date + '.html')
            weather_record[key] = {city_name: {month_date: month_weather}}
print('Finished Scraping.')

# Quiz: Try to convert the "json"-like format to pandas DataFrame
