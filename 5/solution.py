from itertools import takewhile
from collections import deque
import re

with open("./input.txt") as f:
    stack_description = list(takewhile(lambda x: x != "\n", f))
    rows = stack_description.pop()
    row_numbers = re.findall(r"\d+\b", rows)
    max_row = max((int(i) for i in row_numbers))
    stacks = [deque() for _ in range(max_row)]

    for sd in stack_description:
        for i in range(max_row):
            if (ch := sd[i * 4 + 1]) != " ":
                stacks[i].appendleft(ch)

    for instruction in f:
        matches = re.match(
            r"move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)", instruction
        )
        for _ in range(int(matches["move"])):
            stacks[int(matches["to"]) - 1].append(
                stacks[int(matches["from"]) - 1].pop()
            )

    print("".join([s.pop() for s in stacks]))
