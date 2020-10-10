import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyADDx9jMAO2TRePwm5yDG9X-213ihPGRkg"

import geocoder
# Load the Pandas libraries with alias 'pd'
import pandas as pd
import json
import numpy as np
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)

df = pd.read_csv("/Users/annawang/icloud/Documents/Twitter copy/github/covid_id/test.csv")

df.user_location = df.user_location.replace(np.nan, 'Null')

print(df.user_location)
location = df.user_location

places = location.tolist()

address = []
countplace = 0
for place in places:
    if place == 'Null':
        print(countplace)
        countplace = countplace+1
        continue
    g = geocoder.google(place,  key='AIzaSyADDx9jMAO2TRePwm5yDG9X-213ihPGRkg')
    result = g.json
    if result is None:
        continue

    data = json.dumps(result)
    json_to_python = json.loads(data)
    address = json_to_python['address']
    print(countplace)
    print(address)
    df.loc[countplace, 'address'] = address
    countplace = countplace+1

df.to_csv('covid_4_out.csv', encoding='utf-8', na_rep='Null', errors='ignore', index=False)
