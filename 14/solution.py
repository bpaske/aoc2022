import os
import re

rocks = set()
sands = set()
source = (500, 0)

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    pattern = re.compile(r"\d+,\d+")
    for line in f:
        matches = pattern.findall(line)

        for start, finish in zip(matches, matches[1:]):
            start_x, start_y = (int(i) for i in start.split(","))
            finish_x, finish_y = (int(i) for i in finish.split(","))

            for i in range(min(start_x, finish_x), max(start_x, finish_x) + 1):
                for j in range(min(start_y, finish_y), max(start_y, finish_y) + 1):
                    rocks.add((i, j))

max_y = max(y for (_, y) in rocks)
while True:
    current_position = source
    while current_position[1] < max_y:
        x, y = current_position
        if (x, y + 1) not in rocks and not (x, y + 1) in sands:
            current_position = (x, y + 1)

        elif (x - 1, y + 1) not in rocks and not (x - 1, y + 1) in sands:
            current_position = (x - 1, y + 1)

        elif (x + 1, y + 1) not in rocks and not (x + 1, y + 1) in sands:
            current_position = (x + 1, y + 1)
        else:
            sands.add((x, y))
            break
    else:
        break

print(len(sands))
