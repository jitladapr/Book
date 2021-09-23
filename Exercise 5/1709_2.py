count = 0
for x in range(1, 365):
    if x%7 == 0:
        count+=1
    else:
        continue
A = count
print("Numbers of Monday in this year =", A)