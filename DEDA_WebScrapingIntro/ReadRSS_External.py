"""
Description:
 - Scraping Wallstreet Journal RSS feedback, printing out news title and description.
 - Using the attributes and methods of class defined in file "ReadRSSClass.py" from this file.

Usage: Executing this whole file in your IDE or from Terminal.

Author:
 - Junjie Hu, hujunjie@hu-berlin.de
 - Cathy Chen
Last modified date: 19-11-2017
"""

import os
import sys

# sys.path.append(os.getcwd() + '/DEDA_WebScrapingIntro/')
# add the module path to Python searching path
import DEDA_WebScrapingIntro.ReadRSSClass as rrc

# ReadRSSClass is the file name of the module code
r = rrc.ReadRSS("https://feeds.a.dj.com/rss/RSSMarketsMain.xml")
r2 = rrc.ReadRSS("https://feeds.a.dj.com/rss/RSSMarketsMain.xml")

# Here we can print out the object's url in certain format
print(r)
print(f'The type of r is: {type(r)}')

# Here we use == to validate if two responses of two url are equal
if r == r2:
    print("Two urls are the same")
else:
    print("Two urls are not the same")
# Print out the titles
titles = r.get_titles()
# Print out the descriptions
article_types = r.get_specificitem('wsj_articletype')
