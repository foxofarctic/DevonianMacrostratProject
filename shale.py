# csv library
import csv
with open('DevonianColumns.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    # total area of devonian rock found
    totalArea = 0
    # total area of units including shale
    shaleArea= 0
    for row in reader:
        if "hale" in str(row['lith']):
            shaleArea += float(row['col_area'])
        totalArea += float(row['col_area'])
    print("Total Area: " + str(totalArea))
    print("Shale Area: " + str(shaleArea))
    print( "Exposed Devonian Percent Shale: " + str((shaleArea/totalArea) * 100))

