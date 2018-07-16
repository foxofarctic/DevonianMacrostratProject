#import urllib.request, json
import requests, json

# API link for data from pbdb in JSON format
url = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=famennian,famennian&show=genus,timebins'

url2 = 'http://paleobiodb.org/data1.2/taxa/single.json?name=Dascillidae&show=attr'

# receive data from api
response = requests.get(url2)

# create dict object with data response
data = response.json()

# get list of records dicts
records = data['records']

print(recordsDict)
print(type(recordsDict))

