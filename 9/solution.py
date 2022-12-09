import os
from typing import NamedTuple, List, Dict, Callable


class Position(NamedTuple):
    x: int
    y: int


def update_knots(knots: List[Position]):
    for i, (head, tail) in enumerate(zip(knots, knots[1:]), 1):

        x_diff = head.x - tail.x
        y_diff = head.y - tail.y

        if abs(x_diff) == 2 and abs(y_diff) == 2:
            tail = Position(
                tail.x + x_diff // 2,
                tail.y + y_diff // 2,
            )
        elif abs(y_diff) == 2:
            tail = Position(tail.x + x_diff, tail.y + y_diff // 2)
        elif abs(x_diff) == 2:
            tail = Position(tail.x + x_diff // 2, tail.y + y_diff)
        knots[i] = tail


moves: Dict[str, Callable[[Position], Position]] = {
    "R": lambda x: Position(x.x + 1, x.y),
    "L": lambda x: Position(x.x - 1, x.y),
    "U": lambda x: Position(x.x, x.y + 1),
    "D": lambda x: Position(x.x, x.y - 1),
}

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    first_knot_visited_positions = {Position(0, 0)}
    tail_visited_positions = {Position(0, 0)}
    knots = [Position(0, 0) for _ in range(10)]
    for line in f:
        direction, distance = line.strip().split(" ")

        for _ in range(int(distance)):
            knots[0] = moves[direction](knots[0])
            update_knots(knots)
            first_knot_visited_positions.add(knots[1])
            tail_visited_positions.add(knots[9])

print(f"Part 1: {len(first_knot_visited_positions)}")
print(f"Part 2: {len(tail_visited_positions)}")
