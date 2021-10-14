first_day = 4 #first monday
count_monday = 1 #count monday

for i in range(100):
    first_day += 7
    if first_day <= 365:
        count_monday += 1
    else:
        continue
print("Number of monday in this year is",(count_monday))