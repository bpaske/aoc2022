import os, re, collections
from functools import cmp_to_key


pattern = re.compile(r"-?\d+")
max_size = 4000000
# max_size = 20

ranges_by_y_coord = collections.defaultdict(list)

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    for l in f:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, pattern.findall(l))
        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        y_range = range(
            max(0, sensor_y - manhattan_distance),
            min(sensor_y + manhattan_distance, max_size) + 1,
        )

        x_difference_allowed = manhattan_distance - abs(sensor_y - y)
        for y in y_range:
            x_min = max(0, sensor_x - x_difference_allowed)
            x_max = min(sensor_x + x_difference_allowed, max_size)
            if x_min <= x_max:
                ranges_by_y_coord[y].append((x_min, x_max))

for y in range(max_size + 1):
    sorted_range_iterator = iter(sorted(ranges_by_y_coord[y]))
    current_max = -1
    while max_size > current_max:
        try:
            next_start, next_finish = next(sorted_range_iterator)
        except StopIteration:
            print(f"Missing: {current_max +1 }, {y}")
            missing_value = (current_max + 1) * 4000000 + y
            print(missing_value)
            exit(0)

        if next_start > current_max + 1:
            print(f"Missing: {current_max +1 }, {y}")
            missing_value = (current_max + 1) * 4000000 + y
            print(missing_value)
            exit(0)
        current_max = max(current_max, next_finish)
