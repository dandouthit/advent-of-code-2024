import re
sum = 0

with open("../input/day3.txt", 'r') as file:
    line = file.read().replace('\n', '')

mul_pattern = "mul\([0-9]+,[0-9]+\)"
do_pattern = "do\(\)"
dont_pattern = "don't\(\)"

combined_pattern = re.compile(mul_pattern + "|" + do_pattern + "|" + dont_pattern)

matching_list = combined_pattern.findall(line)
enabled = True

def calc_product(item: str) -> int:
    str_list = re.findall(r"[0-9]+", item)
    int_list = [int(x) for x in str_list]
    return int_list[0] * int_list[1]

for item in matching_list:
    if enabled and item[0] == "m":
        sum = sum + calc_product(item)
    elif "n" in item:
        enabled = False
        continue
    elif item[0] == "d":
        enabled = True
        continue
    
print(sum)