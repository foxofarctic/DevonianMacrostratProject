# csv library
import csv

periods = ['SilurianColumns.csv', 'DevonianColumns.csv', 'CarboniferousColumns.csv']
for period in periods:
    
    with open(period, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # total area of devonian rock found
        totalArea = 0
        # total area of units including shale
        shaleArea= 0
        for row in reader:
            if "shale" in str(row['lith']):
                shaleArea += float(row['col_area'])
            totalArea += float(row['col_area'])
        print( "For CSV File: " + period)
        print("Total Area: " + str(totalArea))
        print("Shale Area: " + str(shaleArea))
        print( "Exposed Percent Shale: " + str((shaleArea/totalArea) * 100))

