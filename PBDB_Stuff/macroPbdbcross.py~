# Lucas Estrada (c) 2018
# interpret PBDB data for paleoenvironment

import requests, json
import matplotlib.pyplot as plt

# checks if FAD is within expected time boundary
def inTime(time, boundary):
        return (time <= boundary[0] and time > boundary[1])
                


# method for finding unique paleoenvironments and counting them
def uniqueCounts(recList, boundary):
        envCount = []
        environs = []

        # loop through each dict in records
        for record in recList:

                # checks if 'env' is a valid key in dict
                if ('env' in record) and inTime(record['eag'], boundary):

                        # paleoenvironment
                        env = record['env']

                        # is env unique
                        if not env in environs:

                                # add to list of nique environments
                                environs.append(env)

                                # set count to 1
                                envCount.append(1)
                        else:
                                # otherwise update count 
                                envCount[environs.index(env)] += 1
        # raw data
        print (environs)
        print(envCount)

        # return
        return (environs, envCount)

# environment filter method
# ------------------------------------------------------------------------
def filterEnvis(listOlists):
        # remove carbonate indeterminate and marine indet.
        envNames = listOlists[0]
        paleoCounts = listOlists[1]
        
        if 'carbonate indet.' in envNames:
                paleoCounts.remove(paleoCounts[envNames.index(
                        'carbonate indet.')])
                envNames.remove('carbonate indet.')
        if 'marine indet.' in envNames:
                paleoCounts.remove(paleoCounts[envNames.index(
                        'marine indet.')])
                envNames.remove('marine indet.')
        return (envNames, paleoCounts)
        

# main method
# -----------------------------------------------------------------------

# API links for data from pbdb in JSON format
# Frasnian famennian data
url = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=Frasnian,Famennian&time_rule=overlap&show=env'

# Eifelian-Givetian data
url2 = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=Eifelian,Givetian&time_rule=overlap&show=env'

# list of desired datasets
urls = [(url,'Frasnian-Famennian', [382.7, 358.9] ), (url2, 'Eifelian-Givetian', [393.3, 382.7])]

# loops through the listed datasets
for site in urls:
        # receive data from api - change url for desired dataset
        response = requests.get(site[0])

        # checks for invalid url response
        if str(response) != '<Response [200]>' :
                print("invalid url: " + str(response))
        else:
                # create dict object with data response
                data = response.json()
                
                # get list of records dicts
                records = data['records']

                # counts fossis per unique paleoenvironment
                # filter out unhelpful environments
                paleoenvis = filterEnvis(uniqueCounts(records, site[2]))
                
                envNames = paleoenvis[0]
                paleoCounts = paleoenvis[1]

                # create figures
                plt.figure(figsize=(20,10))
                plt.title(site[1])
                plt.barh(envNames, paleoCounts)


plt.show()
