import re

file_name = 'day_3/01.txt'
corrupted_memory = ""

with open(file_name) as f:
    corrupted_memory = f.read()

pattern = r"mul\((\d+),(\d+)\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

mul_enabled = True
result = 0

index = 0
while index < len(corrupted_memory):
    if corrupted_memory[index:index+4] == "do()":
        mul_enabled = True
        index += 4
    elif corrupted_memory[index:index+7] == "don't()":
        mul_enabled = False
        index += 7
    else:
        match = re.match(pattern, corrupted_memory[index:])
        if match and mul_enabled:
            x, y = match.groups()
            result += int(x) * int(y)
            index += match.end()
        else:
            index += 1

print(f"Sum of the results of all valid mul instructions: {result}")