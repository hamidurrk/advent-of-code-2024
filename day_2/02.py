import numpy as np

file_name = 'day_1/01.txt'
with open(file_name) as f:
    data = [line.strip() for line in f.readlines()]
num_list = []
simscore_list = []

for row in data:
    row = row.split()
    row = [int(i) for i in row]
    num_list.append(row)
    
matrix = np.array(num_list)
left_list = matrix[:, 0]
right_list = matrix[:, 1]

for i in left_list:
    count = 0
    for j in right_list:
        if i == j:
            count+=1
    simscore_list.append(i*count)
    
print(sum(simscore_list))
    
