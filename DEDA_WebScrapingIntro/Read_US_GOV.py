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
