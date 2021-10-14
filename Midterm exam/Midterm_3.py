criteria_A = ["Apr", "Jun", "Sep","Nov"] #30 Days
criteria_B = ["Jan","Mar","May","Jul","Aug","Oct","Dec"] #31 Days
criteria_C = ["Feb"] #28-29 Days

count = 0 #start counting at 0

days = input("Number of days in february: ")

#If february have 29 days
if days == "29":
    for x in criteria_A:
        if x in criteria_A:
            count += (30/2)
        else:
            continue

    for x in criteria_B:
        if x in criteria_B:
            count += (30/2)
            count += 1
        else:
            continue
    for x in criteria_C:
        if x in criteria_C:
            count += (28/2)
            count += 1
        else:
            continue

#If february have 28 days
elif days == "28":
    for x in criteria_A:
        if x in criteria_A:
            count += (30/2)
        else:
            continue

    for x in criteria_B:
        if x in criteria_B:
            count += (30/2)
            count += 1
        else:
            continue
    for x in criteria_C:
        if x in criteria_C:
            count += (28/2)
        else:
            continue

#Number of months
print("Months that have 30 days is",len(criteria_A),"months")
print("Month that have 31 days is",len(criteria_B),"months")
print("Month that have 28 or 29 days is",len(criteria_C),"months")

#Total number of odd days
print("I will travel by NokAir in",int(count),"days")

