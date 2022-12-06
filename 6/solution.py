from itertools import count

with open("./input.txt") as f:
    l = f.readline()
    for i in count(4):
        if len(set(l[i - 4 : i])) == 4:
            print(f"Part 1 answer: {i}")
            break

    for i in count(14):
        if len(set(l[i - 14 : i])) == 14:
            print(f"Part 2 answer: {i}")
            break
