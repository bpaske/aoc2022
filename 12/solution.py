from collections import deque
import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    grid = [list(l.strip()) for l in f]


def find_shortest_path(start):
    Q = deque([(0, start)])
    added = set([start])
    while Q:
        length, (i, j) = Q.popleft()
        current_item = grid[i][j]

        if current_item == "S":
            current_item = "a"

        for next_i, next_j in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (
                next_i >= 0
                and next_i < len(grid)
                and next_j >= 0
                and next_j < len(grid[i])
                and (next_i, next_j) not in added
            ):
                next_item = grid[next_i][next_j]
                if next_item == "E":
                    if current_item == "y" or current_item == "z":
                        return length + 1
                elif ord(next_item) <= ord(current_item) + 1:
                    Q.append((length + 1, (next_i, next_j)))
                    added.add((next_i, next_j))
    return float("inf")


part_one_start = [
    (i, j) for i, r in enumerate(grid) for j, c in enumerate(r) if c == "S"
][0]
print(f"Part 1: {find_shortest_path(part_one_start)}")
starts = [
    (i, j) for i, r in enumerate(grid) for j, c in enumerate(r) if c == "S" or c == "a"
]
print(f"Part 2: {min(find_shortest_path(start) for start in starts)}")
