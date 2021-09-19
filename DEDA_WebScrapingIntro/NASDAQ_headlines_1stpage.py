"""
Description:
 - Scraping the 1st page of news from nasdaq.com.
 - Saving it as .csv file at local disk.
 - Saving web page source code temporarily after request.

Usage: Executing this whole file in your IDE or from Terminal.

Memo:
Toggling refresh to decide if you want to refresh the pages that have been stored locally.

Author: Junjie Hu, hujunjie@hu-berlin.de
Last modified date: 24-10-2019
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
