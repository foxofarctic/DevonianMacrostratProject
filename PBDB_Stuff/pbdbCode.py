#import urllib.request, json
import requests, json
url = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=famennian,famennian&show=genus,timebins'
#response = urllib.request.urlopen(url)
#str_response = response.read().decode('utf-8')
#data = json.loads(str_response)
response = requests.get(url)
todos= json.loads(response.text)
print(type(todos))
#print(data)
#todos[:10]
