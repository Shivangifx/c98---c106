import csv
with open("marks.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

add = 0
for i in range(len(data)):
    #print(data[i][2])
    new_data = data[i][1]
    #print(new_data)
    New_Data = int(data[i][1])
    #print(New_Data)
    add += New_Data
    #print(add)


print(len(data))
print("")
print("")
mean = add/len(data)
print("The average = ",mean)
print("The total = ",add)
