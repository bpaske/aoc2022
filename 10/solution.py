import os

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    answer = 0
    cycle = 0
    x = 1
    for line in f.read().splitlines():
        cycle += 1
        if (cycle - 20) % 40 == 0:
            answer += cycle * x

        if not line == "noop":
            _, value = line.split(" ")
            cycle += 1
            if (cycle - 20) % 40 == 0:
                answer += cycle * x
            x += int(value)
    print(answer)
