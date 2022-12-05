from itertools import takewhile
import re

with open("./input.txt") as f:
    stack_description = list(takewhile(lambda x: x != "\n", f))
    rows = stack_description.pop()
    row_numbers = re.findall(r"\d+\b", rows)
    max_row = max((int(i) for i in row_numbers))
    stacks = [[] for _ in range(max_row)]

    for sd in reversed(stack_description):
        for i in range(max_row):
            if (ch := sd[i * 4 + 1]) != " ":
                stacks[i].append(ch)

    for instruction in f:
        matches = re.match(
            r"move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)", instruction
        )
        move = int(matches["move"])
        from_stack = stacks[int(matches["from"]) - 1]
        to_stack = stacks[int(matches["to"]) - 1]

        to_stack.extend(from_stack[(-1 * move) :])
        del from_stack[-1 * move :]

    print("".join([s.pop() for s in stacks]))
