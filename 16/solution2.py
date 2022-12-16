import os, re, itertools, heapq, collections

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
    av = iter(available_values)
    for time, value in zip(
        range(time_remaining - 1, 0, -2),
        itertools.zip_longest(av, av, fillvalue=0),
    ):
        max_possible_score += time * sum(value)
    return max_possible_score


initial_game_state = (0, ("AA", "AA"), frozenset(), 26)
Q = [(-1 * calculate_max_possible_score(0, frozenset(), 26), initial_game_state)]
current_max = 0
non_negative_valves = len(list(fr for fr in flow_rates.values() if fr > 0))
current_visited_best = collections.defaultdict(lambda: -1)


while Q:
    max_possible_score, (
        current_score,
        current_nodes,
        open_valves,
        time_remaining,
    ) = heapq.heappop(Q)
    if -1 * max_possible_score <= current_max:
        break
    if time_remaining == 1 or len(open_valves) == non_negative_valves:
        current_max = max(current_score, current_max)
        current_visited_best[
            (current_nodes, open_valves, time_remaining)
        ] = current_score
        continue
    if any(
        current_score <= current_visited_best[(current_nodes, open_valves, t)]
        for t in range(time_remaining, 26 + 1)
    ):
        continue
    # Open both
    if (
        flow_rates[current_nodes[0]] > 0
        and current_nodes[0] not in open_valves
        and flow_rates[current_nodes[1]] > 0
        and current_nodes[1] not in open_valves
        and current_nodes[0] != current_nodes[1]
    ):
        new_current_score = current_score + (time_remaining - 1) * (
            flow_rates[current_nodes[0]] + flow_rates[current_nodes[1]]
        )

        new_open_valves = open_valves.union(current_nodes)

        heapq.heappush(
            Q,
            (
                -1
                * calculate_max_possible_score(
                    new_current_score, new_open_valves, time_remaining - 1
                ),
                (
                    new_current_score,
                    current_nodes,
                    new_open_valves,
                    time_remaining - 1,
                ),
            ),
        )
    # Open first

    if flow_rates[current_nodes[0]] > 0 and current_nodes[0] not in open_valves:
        new_current_score = current_score + (time_remaining - 1) * (
            flow_rates[current_nodes[0]]
        )

        new_open_valves = open_valves.union([current_nodes[0]])
        new_max_poss_score = calculate_max_possible_score(
            new_current_score, new_open_valves, time_remaining - 1
        )
        for adjacent_node in G[current_nodes[1]]:
            new_nodes = tuple(sorted((current_nodes[0], adjacent_node)))
            heapq.heappush(
                Q,
                (
                    -1 * new_max_poss_score,
                    (
                        new_current_score,
                        new_nodes,
                        new_open_valves,
                        time_remaining - 1,
                    ),
                ),
            )
    # Open second

    if flow_rates[current_nodes[1]] > 0 and current_nodes[1] not in open_valves:
        new_current_score = current_score + (time_remaining - 1) * (
            flow_rates[current_nodes[1]]
        )

        new_open_valves = open_valves.union([current_nodes[1]])
        new_max_poss_score = calculate_max_possible_score(
            new_current_score, new_open_valves, time_remaining - 1
        )
        for adjacent_node in G[current_nodes[0]]:
            new_nodes = tuple(sorted((current_nodes[1], adjacent_node)))
            heapq.heappush(
                Q,
                (
                    -1 * new_max_poss_score,
                    (
                        new_current_score,
                        new_nodes,
                        new_open_valves,
                        time_remaining - 1,
                    ),
                ),
            )

    # Open neither
    new_max_poss_score = calculate_max_possible_score(
        current_score, open_valves, time_remaining - 1
    )
    new_adjacent_nodes = {
        tuple(sorted((i, j))) for i in G[current_nodes[0]] for j in G[current_nodes[1]]
    }
    for new_nodes in new_adjacent_nodes:
        heapq.heappush(
            Q,
            (
                -1 * new_max_poss_score,
                (
                    current_score,
                    new_nodes,
                    open_valves,
                    time_remaining - 1,
                ),
            ),
        )

    current_visited_best[(current_nodes, open_valves, time_remaining)] = current_score

print(current_max)
