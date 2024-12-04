import re


file_name = 'day_3/01.txt'
# corrupted_memory = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
corrupted_memory = ""

with open(file_name) as f:
    corrupted_memory = f.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, corrupted_memory)
result = sum(int(x) * int(y) for x, y in matches)

print(f"Sum of the results of all valid mul instructions: {result}")