import numpy as np

file_name = 'day_2/01.txt'
with open(file_name) as f:
    data = [line.strip() for line in f.readlines()]
num_list = []

for row in data:
    row = row.split()
    row = [int(i) for i in row]
    num_list.append(row)

def is_increasing(row):
    prev = None
    for x in row:
        if prev is not None:
            if prev >= x:
                return False
        prev = x
    return True

def is_decreasing(row):
    prev = None
    for x in row:
        if prev is not None:
            if prev <= x:
                return False
        prev = x
    return True

def is_difference_valid(row):
    for i in range(1, len(row)):
        diff = abs(row[i] - row[i - 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe(row):
    if (is_increasing(row) or is_decreasing(row)) and is_difference_valid(row):
        return True
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if (is_increasing(new_row) or is_decreasing(new_row)) and is_difference_valid(new_row):
            return True
    return False

safe_reports = 0
for row in num_list:
    if is_safe(row):
        safe_reports += 1

print(f"Number of safe reports: {safe_reports}")