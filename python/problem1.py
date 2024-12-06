#placeholder
with open("../input/day1.txt") as inp:
    print( list(zip(*(line.strip().split('\t') for line in inp))) )
