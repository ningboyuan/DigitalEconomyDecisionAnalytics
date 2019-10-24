import requests
import json
import pandas as pd

"""
Collecting the number of US passport applications each fiscal year
"""
url = 'https://cadatacatalog.state.gov/dataset/0b1b5da3-9c85-43b9-91b1-54792bc7d552/resource/bed04310-9048-4f8d-ba42-9ea91c6d272f/download/passportapplicationbyfiscalyear.json'

response = requests.get(url)
content = json.loads(response.content)

Year = [item['Year'] for item in content]
Count = [item['Count'] for item in content]

Info = zip(Year, Count)
PassportData = pd.DataFrame(list(Info), columns=['Year', 'Count'])
