# csv library
import csv

# filenames of data
periods = ['SilurianColumns.csv', 'DevonianColumns.csv', 'CarboniferousColumns.csv']

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

        # Print Data
        print( "For CSV File: " + period)    
        print("Total Area: " + str(totalArea))
        print("Shale Area: " + str(shaleArea))
        print("Fossiliferous Area: " + str(fossilArea))
        print( "Exposed Percent Shale: " + str(percentShale) + "\n" )
