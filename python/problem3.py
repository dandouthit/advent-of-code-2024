import re
sum = 0

with open("/home/dandouthit/advent-of-code-2024/input/day3.txt", 'r') as file:
    line = file.read().replace('\n', '')

matching_list = re.findall(r"mul\([0-9]+,[0-9]+\)", line)

for item in matching_list:
    str_list = re.findall(r"[0-9]+", item)
    int_list = [int(x) for x in str_list]
    sum = sum + int_list[0] * int_list[1]

print(sum)