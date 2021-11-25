import pandas as pds
from math import sin,cos,atan2,radians,sqrt
def verticaldistance (baro1, baro2):
    va= baro2-baro1
    return abs(va)
def horizontaldistance (latA,lonA,latB,lonB):
    R = 3437.67

    latA = radians(latA)
    lonA = radians(lonA)
    latB = radians(latB)
    lonB = radians(lonB)

    dlon = lonB - lonA
    dlat = latB - latA

    a = sin(dlat/2)**2 + cos(latA) * cos(latB) * sin(dlon/2)**2
    b = 2 * atan2(sqrt(a), sqrt(1-a))

    distance = R*b
    return distance
dataf = pds.read_csv("D:\Day4\day4.csv")
dataf = dataf.drop(columns=['velocity', 'onground', 'icao24', 'heading', 'vertrate', 'alert', 'spi', 'hour', 'squawk', 'geoaltitude', 'lastposupdate', 'lastcontact'])
dataf = dataf.sort_values(by="time")
dataf = dataf.reset_index(drop = True)
print(dataf)
print(dataf.index)
countbaro=0
counthorizontal=0
#vertical
#for x in dataf.index:
#    y=x+1
#    if y not in dataf.index:
#        break
#    while dataf.at[y, 'time']==dataf.at[x, 'time']:
#        if verticaldistance(dataf.at[x,'baroaltitude'], dataf.at[y,'baroaltitude']) < 304.8:
#            countbaro+=1
#            print(countbaro)
#        y+=1
#        if y not in dataf.index:
#            break
for x in dataf.index:
    y=x+1
    if y not in dataf.index:
        break
    while dataf.at[y, 'time']== dataf.at[x, 'time']:
        if horizontaldistance(dataf.at[x, 'lat'], dataf.at[x, 'lon'], dataf.at[y, 'lat'], dataf.at[y, 'lon'])<3:
            counthorizontal+=1
            print(counthorizontal)
        y+=1
        if y not in dataf.index:
            break
#print("done", countbaro, "final")
print("done", counthorizontal, "final")