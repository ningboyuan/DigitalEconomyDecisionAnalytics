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
# Print out the article type
article_types = r.get_specificitem('wsj_articletype')


"""
Author:
 - Cathy Chen
"""

import requests
import xml.dom.minidom

response = requests.get(
    "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Datasets/daily_treas_bill_rates.xml")
content = response.content
dataDOM = xml.dom.minidom.parseString(content)

import requests
import json
import pandas as pd

"""
Collecting the number of US passport applications each fiscal year
"""

url ='https://cadatacatalog.state.gov/dataset/a765ec3a-cf98-4722-a562-40c3f03d24d5/resource/a3bb04a8-dcda-4a03-ba87-e4ec63f2c4c3/download/passportapplicationbyfiscalyear.json'

response = requests.get(url)
content = json.loads(response.content)

Year = [item['Year'] for item in content]
Count = [item['Count'] for item in content]

Info = zip(Year, Count)
PassportData = pd.DataFrame(list(Info), columns=['Year', 'Count'])
print(PassportData)

"""
Description:
 - Demonstrating how to create a class
 - Inheritance and Instantiation
Usage: Executing this whole file in your IDE or from Terminal or executing line by line in iPython.
Author: Junjie Hu, hujunjie@hu-berlin.de
Last modified date: 19-11-2017
"""


# Simple class


class Person(object):
    # The class Person is inherited from class object
    def __init__(self, first, last, gender, age):
        # self is the default argument that points to the instance
        # Using __init__ to initialize a class to take arguments
        self.first_name = first
        self.last_name = last
        self.gender = gender
        self.age = age


class Student(Person):
    # The class Student inherited from class Person
    def __init__(self, first, last, gender, age, school):
        # super() method allows us to handle the arguments from parent class without copying
        super().__init__(first, last, gender, age)
        # Child class can also be added new arguments
        self.school = school

    def describe(self):
        # describe is a method of class Student
        print('{0} {1} is a {2} years old {3} who studies at {4}.'.format(
            self.first_name,
            self.last_name,
            self.age,
            self.gender,
            self.school))


# stu_1 is an instance of class Student
stu_1 = Student('Jon', 'Doe', 'male', 10, 'C_School')
print("Is Student a subclass of Person: ", issubclass(Student, Person))
print("Is stu_1 an instance of Student: ", isinstance(stu_1, Student))
# Using the attributes in the object stu_1
print(stu_1.school)
# Using the methods in the object stu_1
stu_1.describe()

"""
Description:
 - This class is for API StockTwits
 - Usage for searching and retrieving
Usage: Using this class from external files
Author: Roméo Després <romeo.despres@ens-rennes.fr>
Last modified date: 27-11-2017
"""


import requests

class StockTwitsApi:

  def __init__(self):
    self.base = "https://api.stocktwits.com/api/2/"
    self.token = ""

  def login(self, token):
    self.token = token
    return(self)

  def search(self, mode=None, **kwargs):

    """ mode can have value None, "users" or "symbols"."""

    url = self.base + "search{}.json".format("" if mode is None else "/" + mode)
    if self.token != "":
      kwargs.update({"access_token": self.token})
    result = requests.get(url, params=kwargs)
    return(result)

  def stream_symbol(self, id, **kwargs):
    url = self.base + "streams/symbol/{}.json".format(id)
    if self.token != "":
      kwargs.update({"access_token": self.token})
    result = requests.get(url, params=kwargs)
    return(result)