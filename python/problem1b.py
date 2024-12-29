list1 = []
list2 = []
score = 0

with open("/../input/day1.txt", 'r') as file:
    for line in file:
        items = line.split()
        list1.append(int(items[0]))
        list2.append(int(items[1]))


for item in list1:
    score = score + (item * list2.count(item))

print(score)