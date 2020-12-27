import csv 
with open('data.csv') as a:
    reader = csv.reader(a)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][2]
    print(n_num)
    new_data.append(float(n_num))
    print(new_data)

n = len(new_data)
total = 0
for x in new_data:
    total+=x

mean = total / n

print(mean)