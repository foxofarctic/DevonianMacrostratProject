# Lucas Estrada (c) 2018
#compare devonian, silurian, carbniferous shale areas
#
# csv library
import csv
import matplotlib.pyplot as plt

# filenames of data
periods = ['SilurianColumns.csv', 'DevonianColumns.csv', 'CarboniferousColumns.csv']

# total area of exposed rock found in period
totalAreaMas = []
# total area of units including shale
shaleAreaMas = []
# fossiliferous areas
fossilAreaMas = []
index = 0

for period in periods:

    with open(period, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # total area of exposed rock found in period
        totalArea = 0
        # total area of units including shale
        shaleArea = 0
        # fossiliferous areas
        fossilArea = 0
        
        for row in reader:
            localArea = float(row['col_area'])
            if int(row['pbdb_collections']) > 0:
                fossilArea += localArea
                
            if "shale" in str(row['lith']):
                shaleArea += localArea
            totalArea += localArea

    # Calculate Percent Shale
    percentShale = (shaleArea/totalArea) * 100.0

    # add data to master lists
    totalAreaMas.append(totalArea)
    shaleAreaMas.append(shaleArea)
    fossilAreaMas.append(fossilArea)
        
    # Print Data
    print( "For CSV File: " + period)    
    print("Total Area: " + str(totalArea))
    print("Shale Area: " + str(shaleArea))
    print("Fossiliferous Area: " + str(fossilArea))
    print( "Exposed Percent Shale: " + str(percentShale) + "\n" )

    index += 1
