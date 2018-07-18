# Lucas Estrada (c) 2018
# interpret PBDB data for paleoenvironment

import requests, json
import matplotlib.pyplot as plt

# API link for data from pbdb in JSON format
url = 'https://paleobiodb.org/data1.2/occs/list.json?interval=gorstian,famennian&time_rule=overlap&show=genus,timebins'

# smaller test dataset- only lochkovian


# receive data from api - change url for desired dataset
response = requests.get(url2)

# checks for invalid url response
if str(response) != '<Response [200]>' :
        print("invalid url: " + str(response))
else:
    # create dict object with data response
    data = response.json()
    
    # get list of records dicts
    records = data['records']
    print(records[1])            
