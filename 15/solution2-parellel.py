import os, re
from multiprocessing import Pool, Event
import functools
import concurrent.futures

pattern = re.compile(r"-?\d+")
max_size = 4000000
# max_size = 20


def search(lines, y_range):
    for y in range(*y_range):
        ranges = []
        for line in lines:
            sensor_x, sensor_y, beacon_x, beacon_y = line
            manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

            x_difference_allowed = manhattan_distance - abs(sensor_y - y)
            x_min = max(0, sensor_x - x_difference_allowed)
            x_max = min(sensor_x + x_difference_allowed, max_size)
            if x_min <= x_max:
                ranges.append((x_min, x_max))

        sorted_range_iterator = iter(sorted(ranges))
        current_max = -1
        while max_size > current_max:
            try:
                next_start, next_finish = next(sorted_range_iterator)
            except StopIteration:
                print(f"Missing: {current_max +1 }, {y}")
                missing_value = (current_max + 1) * 4000000 + y
                print(missing_value)
                return

            if next_start > current_max + 1:
                print(f"Missing: {current_max +1 }, {y}")
                missing_value = (current_max + 1) * 4000000 + y
                print(missing_value)
                return
            current_max = max(current_max, next_finish)


def main():
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        lines = [list(map(int, pattern.findall(l))) for l in f]

        with Pool(10) as p:
            fn = functools.partial(search, lines)
            step_size = max_size // 10
            p.map(
                fn,
                list(
                    zip(
                        range(0, 10 * step_size, step_size),
                        range(1 * step_size, 11 * step_size, step_size),
                    )
                ),
            )


if __name__ == "__main__":
    main()
