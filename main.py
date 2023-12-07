import requests
import json
import config

# limit and offset are included in the URL
offset = 1
limit = 1000
token = config.NOAA_TOKEN

# ID for New Castle County DE. Found using previous locations lab
# FIPS:10003

for i in range(2):
    url = f"https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&offset={offset}&limit={limit}"
    response = requests.get(url, headers={'token': token})

    with open(f'data/daily_summaries/daily_summaries_FIPS10003_jan_2018_{i}.json', 'w') as file:
        json.dump(response.json(), file)

    offset += limit
