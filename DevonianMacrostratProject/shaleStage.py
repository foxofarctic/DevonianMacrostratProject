# Lucas Estrada (c) 2018
# compare shale area vs total area exposed rock for each stage of the devonian
# also fossiliferous area

# csv library
import csv
import matplotlib.pyplot as plt

# filenames of data
periods = ['DevonianColumns.csv']

# stage data [b_age,t_age,total area, total shale area, total fossil area]
fammenianT = [372.2,358.9,0,0,0,'Fammenian',0,0]
frasnianT = [382.7,372.2,0,0,0,'Frasnian',0,0]
givetianT = [387.7,382.7,0,0,0,'Givetian',0,0]
eifelianT = [393.3,387.7,0,0,0,'Eifelian',0,0]
emsianT = [407.6,393.3,0,0,0,'Emsian',0,0]
pragianT = [410.8,407.6,0,0,0,'Pragian',0,0]
lochkovianT = [419.2,410.8,0,0,0,'Lochkovian',0,0]

# constants for stage data indices
B_AGE = 0
T_AGE = 1
TOTAL_AREA = 2
SHALE_AREA = 3
FOSSIL_AREA = 4
STAGE_NAME = 5
TOTAL_LOCALITIES = 6
MUDSTONE_AREA = 7

#constants for rockType
ROCK = 0
THICKNESS = 1

# list of stages/ times, to use:
# [controls index of which stage] [controls index of stageData]
stageTimes = [lochkovianT, pragianT, emsianT, eifelianT, givetianT, frasnianT, fammenianT]

for period in periods:
    with open(period, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:

            # retrieve some csv Data
            localArea = float(row['col_area'])
            b_age = float(row['b_age'])
            t_age = float(row['t_age'])

            # lithology rock type/ proportional thickness array
            rockTypes = []
            
            # remove long range localities - set to <25 mya
            if (b_age - t_age) < 25:

                # parse through lith for rock type/ proportional thickness data
                lithString = str(row['lith'])
                while '|' in lithString:
                    lithSub = lithString[0:lithString.find('|')]
                    rockTypes.append([lithSub[0:lithSub.find('~')-2],
                                      float(lithSub[lithSub.find('~')+2 : len(lithSub)])])
                    lithString = lithString[lithString.find('|')+1:len(lithString)]

                rockTypes.append([lithString[0:lithString.find('~')-2],
                                  float(lithString[lithString.find('~')+2 : len(lithString)])])
                    
                # perform for each stage
                for stage in stageTimes:

                    # start, ends, or passes through stage?
                    if ((b_age > stage[B_AGE] and t_age < stage[B_AGE]) or
                        (b_age < stage[B_AGE] and b_age > stage[T_AGE]) or
                        (t_age < stage[B_AGE] and t_age > stage[T_AGE])):
                    #if b_age < stage[B_AGE] and t_age > stage[T_AGE]:

                        # fosiliferous?
                        if int(row['pbdb_collections']) > 0:
                            stage[FOSSIL_AREA] += localArea

                        # check for rock Types
                        for rock in rockTypes:

                            # check shale, thickness > .2
                            if ('shale siliciclastic' in rock[ROCK]
                                and rock[THICKNESS] > 0.2):
                                stage[SHALE_AREA] += localArea

                            # check mudstone, thickness > 0.0
                            if ('mudstone siliciclastic' in  rock[ROCK]
                                and rock[THICKNESS] > 0.0):
                                stage[MUDSTONE_AREA] += localArea
                                
                        # add area and locality
                        stage[TOTAL_AREA] += localArea
                        stage[TOTAL_LOCALITIES] += 1

    # Arrays of various rock type Areas
    shaleAreaArr = []
    stageB_ageArr = []
    mudstoneAreaArr = []
    
    # loop through various stages for data printing
    for stage in stageTimes:
        
        # Print Data
        print( "For CSV File: " + period)
        print( "Stage: " + str(stage[STAGE_NAME]))
        print( "Total Localities: " + str(stage[TOTAL_LOCALITIES]))
        print("Total Area: " + str(stage[TOTAL_AREA]))
        print("Shale Area: " + str(stage[SHALE_AREA]))
        print("Fossiliferous Area: " + str(stage[FOSSIL_AREA]))

        
       
        
        # Calculate Percent Shale
        if stage[TOTAL_AREA] != 0:
            percentShale = (stage[SHALE_AREA]/stage[TOTAL_AREA]) * 100.0
            percentFossil = (stage[FOSSIL_AREA]/stage[TOTAL_AREA]) * 100.0
            percentMudstone = (stage[MUDSTONE_AREA]/stage[TOTAL_AREA]) * 100.0
            
            # arrays for scatter plot
            shaleAreaArr.append(percentShale)
            stageB_ageArr.append(stage[STAGE_NAME])
            mudstoneAreaArr.append(percentMudstone)
            
            print( "Exposed Percent Fossiliferous Area: " + str(percentFossil))
            print( "Exposed Percent Shale: " + str(percentShale))
            print( "Exposed Percent Mudstone: " + str(percentMudstone))
        print("-------------------------------------------------------")

# plot of shale data
plt.figure(1)
plt.plot(stageB_ageArr, shaleAreaArr, 'o-')
plt.ylabel('Percent Shale')
plt.xlabel('Stage')
plt.title('Percent Shale through Devonian')

# plot of mudstone data
plt.figure(2)
plt.plot(stageB_ageArr, mudstoneAreaArr, 'o-')
plt.title('Percent Mudstone through Devonian')

plt.show()



