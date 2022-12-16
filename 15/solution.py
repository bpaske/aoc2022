import os, re


pattern = re.compile(r"-?\d+")
senors = set()
beacons = set()
beacon_not_present = set()
interested_row = 2000000


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    for l in f:
        sensor_x, sensor_y, beacon_x, beacon_y = map(int, pattern.findall(l))
        manhattan_distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)

        if sensor_y == interested_row:
            senors.add(sensor_x)
        if beacon_y == interested_row:
            beacons.add(beacon_x)

        x_difference_allowed = manhattan_distance - abs(sensor_y - interested_row)
        beacon_not_present.update(
            range(sensor_x - x_difference_allowed, sensor_x + x_difference_allowed + 1)
        )

print(len(beacon_not_present - beacons))
