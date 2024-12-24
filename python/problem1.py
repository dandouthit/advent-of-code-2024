list1 = []
list2 = []

with open("/home/dandouthit/advent-of-code-2024/input/day1.txt", 'r') as file:
    for line in file:
        items = line.split()
        list1.append(items[0])
        list2.append(items[1])

list1.sort()
list2.sort()
distance = 0

for i in range(len(list1)):
    distance += abs(int(list1[i]) - int(list2[i]))

print(distance)