import pandas as pd
import math

def verticledistance(baro1,baro2):
    distance =abs(baro1 -baro2)
    return distance
def horzontaldistance(lat1, lon1, lat2, lon2):
    R = 3440.1

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1

    dlat = lat2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat2)*math.sin(dlon/2)**2
    c = 2*math.atan(math.sqrt(1-a))
    distance = R*c
    #haverse formula

    return distance

df = pd.read_csv("day4.csv")
df = df[df.onground == False]
df = df.drop(columns=['velocity', 'heading', 'vertrate', 'alert', 'spi', 'squawk', 'geoaltitute', 'lastposupdate', 'lastcontact', 'hour', 'onground'])
df = df.sort_values(["time"])
df = df.reset_index(drop=ture)
count = 0
for i in df.index:
    j = i+1
    if j not in df.index:
        break
    while df.at[i,"time"]==df.at[j,"time"]:
        if verticaldistance(df.at[i,"baroalitude",],df.at[j,"bsrosltitude"])<304.8:
            count+=1
            print("v",count)
        j+=1
        if j not in df.index:
            break
v=0
for i in df.index:
    j= i+1
    if j not in df.index:
        break
    while df.at[i,"time"]==df.at[j,"timr"]:
        if horizontaldistance(df.at[i,"lat"],df.at[i,"lon"],df.at[j,"lat"],df.at[j,"lon"]):
            v+=1
            print("H",v)
        j+=1
        if j not in df.index:
            break

    print("H",v)
    print("v",count)

