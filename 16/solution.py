import os, re, itertools, heapq, operator, functools

pattern = r"Valve (?P<valve>\w+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<adjacent_valves>.*)"
flow_rates = {}
G = {}

with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    for l in f:
        matches = re.match(pattern, l.strip())
        valve = matches.group("valve")
        flow_rates[valve] = int(matches.group("rate"))
        G[valve] = [v.strip() for v in matches.group("adjacent_valves").split(",")]


def calculate_max_possible_score(current_score, open_valves, time_remaining):
    available_values = sorted(
        [v for k, v in flow_rates.items() if k not in open_valves], reverse=True
    )
    max_possible_score = current_score
    for time, value in zip(range(time_remaining - 1, 0, -2), iter(available_values)):
        max_possible_score += time * value
    return max_possible_score


initial_game_state = (0, "AA", frozenset(), 30)
Q = [(-1 * calculate_max_possible_score(0, frozenset(), 30), initial_game_state)]
current_max = 0
non_negative_valves = len(list(fr for fr in flow_rates.values() if fr > 0))

while Q:
    max_possible_score, (
        current_score,
        current_node,
        open_valves,
        time_remaining,
    ) = heapq.heappop(Q)
    if -1 * max_possible_score < current_max:
        break
    if time_remaining == 1 or len(open_valves) == non_negative_valves:
        current_max = max(current_score, current_max)
    else:
        if flow_rates[current_node] > 0 and current_node not in open_valves:
            new_current_score = (
                current_score + (time_remaining - 1) * flow_rates[current_node]
            )

            new_open_valves = open_valves.union([current_node])
            heapq.heappush(
                Q,
                (
                    -1
                    * calculate_max_possible_score(
                        new_current_score, new_open_valves, time_remaining - 1
                    ),
                    (
                        new_current_score,
                        current_node,
                        new_open_valves,
                        time_remaining - 1,
                    ),
                ),
            )
        for adjacent_node in G[current_node]:
            heapq.heappush(
                Q,
                (
                    -1
                    * calculate_max_possible_score(
                        current_score, open_valves, time_remaining - 1
                    ),
                    (current_score, adjacent_node, open_valves, time_remaining - 1),
                ),
            )


print(current_max)
