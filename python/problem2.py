safe_count = 0

def line_safe(int_list):
    if (is_increasing(int_list) or is_decreasing(int_list)) and diff_small(int_list):
        return True
    return False

def is_increasing(lst: list[int]) -> bool:
    """Checks if a list of integers is strictly increasing."""
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True

def is_decreasing(lst: list[int]) -> bool:
    """Checks if a list of integers is strictly decreasing."""
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            return False
    return True

def diff_small(int_list):
    for i in range(1, len(int_list)):
        if abs(int_list[i] - int_list[i -1]) > 3:
            return False
    return True


with open("../input/day2.txt", 'r') as file:
    for line in file:
        items = line.split()
        int_list = [int(x) for x in items]

        safe_count = safe_count + int(line_safe(int_list))

print(safe_count)