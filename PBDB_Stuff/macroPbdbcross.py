# Lucas Estrada (c) 2018
# combine macrostrat and pbdb code

import requests, json
import matplotlib.pyplot as plt

# get pbdb data
# ------------------------------------------------------------------------

# loops through the listed datasets
def getData(url):
        response = requests.get(url)
        # checks for invalid url response
        if str(response) != '<Response [200]>' :
                print("invalid url: " + str(response))
                return []
        else:
                # create dict object with data response
                data = response.json()
                # get list of records dicts
                return(data['records'])

# main method
# -----------------------------------------------------------------------

# API links for data from pbdb in JSON format
# Frasnian famennian data
url = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=Frasnian,Famennian&time_rule=overlap&show=env'

# Eifelian-Givetian data
url2 = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=Eifelian,Givetian&time_rule=overlap&show=env'

macroUrl = 'https://macrostrat.org/api/v2/units?interval_name=Devonian'

# list of desired datasets
urls = [(macroUrl, [419.2, 358.9]),(url,'Frasnian-Famennian', [382.7, 358.9] ), (url2, 'Eifelian-Givetian', [393.3, 382.7])]

#for site in urls:
        # receive data from api - change url for desired dataset
print(getData(urls[1][0]))
