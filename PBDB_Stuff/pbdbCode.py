import requests, json
import matplotlib.pyplot as plt

NAMES = ['Lochkovian','Pragian','Emsian','Eifelian','Givetian','Frasnian','Famennian','Non Devonian']
LOCHKOVIAN = 0
PRAGIAN = 1
EMSIAN = 2
EIFELIAN = 3
GIVETIAN = 4
FRASNIAN = 5
FAMENNIAN = 6
NONDEVONIAN = 7

# checks which stage the inputted time is in
def stageSort(lag):
    
    if lag >= 359.0 and lag <= 372.0:
        return FAMENNIAN
    elif lag >= 372.0 and lag <= 383.0:
        return FRASNIAN
    elif lag >= 383.0 and lag <= 388.0:
        return GIVETIAN
    elif lag >= 388.0 and lag <= 393.0:
        return EIFELIAN
    elif lag >= 393.0 and lag <= 408.0:
        return EMSIAN
    elif lag >= 408.0 and lag <= 411.0:
        return PRAGIAN
    elif lag >= 411.0 and lag <= 419.0:
        return LOCHKOVIAN
    else:
        return NONDEVONIAN


# main method
# API link for data from pbdb in JSON format
url = 'https://paleobiodb.org/data1.2/occs/list.json?interval=lochkovian,famennian&time_rule=overlap&show=genus,timebins'

url2 = 'https://paleobiodb.org/data1.2/occs/list.json?interval=lochkovian,lochkovian&time_rule=overlap&show=genus,timebins'

# receive data from api
response = requests.get(url2)

if str(response) != '<Response [200]>' :
    print("invalid url: " + str(response))
else:

    # create dict object with data response
    data = response.json()

    # get list of records dicts
    records = data['records']

    eag_stageCount = [0,0,0,0,0,0,0,0]
    lag_stageCount = [0,0,0,0,0,0,0,0]
    eagOverLag = [0,0,0,0,0,0,0,0]
    for record in records:
        eag_stageCount[stageSort(record['eag'])] += 1
        lag_stageCount[stageSort(record['lag'])] += 1
    
    print("origination count: " + str(eag_stageCount))
    print("extinction count: " + str(lag_stageCount))
    print("total: " + str(len(records)))

    
    plt.figure(figsize=(20,10))
    plt.subplot(2,1,1)
    plt.bar(NAMES, eag_stageCount, align='center', alpha=0.5)
    plt.ylabel('Total Origination')
    plt.title('Origination Through the Devonian')

    plt.subplot(2,1,2)
    plt.title('Extinction through the Devonian')
    plt.bar(NAMES, lag_stageCount, align='center', alpha=0.5)
    plt.ylabel('Total Extinction')

    #i = 0
    #for stg in eag_stageCount:
    #    eagOverLag[i] = float(stg)/float(lag_stageCount[i])
     #   i+=1
    #plt.subplot(2,2,2)
    #plt.title('Origination/Extinction')
    #plt.bar(NAMES, eagOverLag, align='center', alpha=0.5)
    plt.show()
