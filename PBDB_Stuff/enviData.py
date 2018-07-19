# Lucas Estrada (c) 2018
# interpret PBDB data for paleoenvironment

import requests, json
import matplotlib.pyplot as plt

# API links for data from pbdb in JSON format
# Frasnian famennian data
url = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=Frasnian,Famennian&time_rule=overlap&show=env'

# Eifelian-Givetian data
url2 = 'https://paleobiodb.org/data1.2/occs/list.json?datainfo&rowcount&interval=Eifelian,Givetian&time_rule=overlap&show=env'

# list of desired datasets
urls = [(url,'Frasnian-Famennian' ), (url2, 'Eifelian-Givetian')]

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

                # list of unique paleoenvironment names
                environs = []

                # counts of each paleoenvironment - corresponds to  environs
                envCount = []
                
                # get list of records dicts
                records = data['records']

                # loop through each dict in records
                for record in records:

                        # checks if 'env' is a valid key in dict
                        if 'env' in record:

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
                # raw data printout
                print(environs)
                print(envCount)

                # remove carbonate indeterminate and marine indet.
                if 'carbonate indet.' in environs:
                        envCount.remove(envCount[environs.index('carbonate indet.')])
                        environs.remove('carbonate indet.')
                if 'marine indet.' in environs:
                        envCount.remove(envCount[environs.index('marine indet.')])
                        environs.remove('marine indet.')
                

                # create figures
                plt.figure(figsize=(20,10))
                plt.title(site[1])
                plt.barh(environs, envCount)


plt.show()

                
