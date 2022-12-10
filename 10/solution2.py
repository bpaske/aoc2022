import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    solution = []
    cycle = 0
    x = 1
    for line in f.read().splitlines():
        if abs(cycle % 40 - x) <= 1:
            solution.append("#")
        else:
            solution.append(".")
        cycle += 1

        if not line == "noop":
            _, value = line.split(" ")
            if abs(cycle % 40 - x) <= 1:
                solution.append("#")
            else:
                solution.append(".")
            cycle += 1
            x += int(value)
    for i in range(0, 6):
        print("".join(solution[i * 40 : (i + 1) * 40]))
