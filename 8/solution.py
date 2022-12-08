import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    grid = []

    for line in f:
        grid.append([int(c) for c in line.strip()])

visible_trees = set()

depth = len(grid)
width = len(grid[0])

for y in range(depth):
    current_tallest = -1
    for x in range(width):
        if grid[y][x] > current_tallest:
            visible_trees.add((x, y))
            current_tallest = grid[y][x]

for y in range(depth):
    current_tallest = -1
    for x in reversed(range(width)):
        if grid[y][x] > current_tallest:
            visible_trees.add((x, y))
            current_tallest = grid[y][x]

for x in range(width):
    current_tallest = -1
    for y in range(depth):
        if grid[y][x] > current_tallest:
            visible_trees.add((x, y))
            current_tallest = grid[y][x]

for x in range(width):
    current_tallest = -1
    for y in reversed(range(depth)):
        if grid[y][x] > current_tallest:
            visible_trees.add((x, y))
            current_tallest = grid[y][x]

print(f"Part 1 answer: {len(visible_trees)}")

highest_scenic_score = 0

for x in range(width):
    for y in range(depth):
        tree_height = grid[y][x]
        up_view = 0
        for i in reversed(range(y)):
            up_view += 1
            if grid[i][x] >= tree_height:
                break
        down_view = 0
        for i in range(y + 1, depth):
            down_view += 1
            if grid[i][x] >= tree_height:
                break
        left_view = 0
        for i in reversed(range(x)):
            left_view += 1
            if grid[y][i] >= tree_height:
                break
        right_view = 0
        for i in range(x + 1, width):
            right_view += 1
            if grid[y][i] >= tree_height:
                break
        current_scenic_score = up_view * down_view * right_view * left_view

        if current_scenic_score > highest_scenic_score:
            highest_scenic_score = current_scenic_score

print(f"Part 2 answer: {highest_scenic_score}")
