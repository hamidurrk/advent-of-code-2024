import numpy as np

file_name = 'day_1/01.txt'
with open(file_name) as f:
    data = [line.strip() for line in f.readlines()]
num_list = []
distance_list = []

for row in data:
    row = row.split()
    row = [int(i) for i in row]
    num_list.append(row)
    
matrix = np.array(num_list)
left_list = np.sort(matrix[:, 0])
right_list = np.sort(matrix[:, 1])

for i, j in zip(left_list, right_list):
    distance_list.append(abs(i - j))

print(sum(distance_list))
    
