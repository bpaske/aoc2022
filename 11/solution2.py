class Monkey:
    # n = 13 * 17 * 19 * 23
    n = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

    def __init__(self, operation, test, starting_items):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.processed_items = 0

    def process_items(self):
        while self.items:
            self.processed_items += 1
            current_item = self.items.pop()
            current_item = self.operation(current_item)
            yield self.test(current_item), current_item % self.n

    def add_item(self, item):
        self.items.append(item)


# monkeys = [
#     Monkey(
#         starting_items=[79, 98],
#         operation=lambda x: x * 19,
#         test=lambda x: 3 if x % 23 else 2,
#     ),
#     Monkey(
#         starting_items=[54, 65, 75, 74],
#         operation=lambda x: x + 6,
#         test=lambda x: 0 if x % 19 else 2,
#     ),
#     Monkey(
#         starting_items=[79, 60, 97],
#         operation=lambda x: x * x,
#         test=lambda x: 3 if x % 13 else 1,
#     ),
#     Monkey(
#         starting_items=[74],
#         operation=lambda x: x + 3,
#         test=lambda x: 1 if x % 17 else 0,
#     ),
#  ]

monkeys = [
    Monkey(
        starting_items=[91, 66],
        operation=lambda x: x * 13,
        test=lambda x: 2 if x % 19 else 6,
    ),
    Monkey(
        starting_items=[78, 97, 59],
        operation=lambda x: x + 7,
        test=lambda x: 3 if x % 5 else 0,
    ),
    Monkey(
        starting_items=[57, 59, 97, 84, 72, 83, 56, 76],
        operation=lambda x: x + 6,
        test=lambda x: 7 if x % 11 else 5,
    ),
    Monkey(
        starting_items=[81, 78, 70, 58, 84],
        operation=lambda x: x + 5,
        test=lambda x: 0 if x % 17 else 6,
    ),
    Monkey(
        starting_items=[60],
        operation=lambda x: x + 8,
        test=lambda x: 3 if x % 7 else 1,
    ),
    Monkey(
        starting_items=[57, 69, 63, 75, 62, 77, 72],
        operation=lambda x: x * 5,
        test=lambda x: 4 if x % 13 else 7,
    ),
    Monkey(
        starting_items=[73, 66, 86, 79, 98, 87],
        operation=lambda x: x * x,
        test=lambda x: 2 if x % 3 else 5,
    ),
    Monkey(
        starting_items=[95, 89, 63, 67],
        operation=lambda x: x + 2,
        test=lambda x: 4 if x % 2 else 1,
    ),
]

for _ in range(10000):
    for k, v in enumerate(monkeys):
        for next_monkey, worry_score in v.process_items():
            monkeys[next_monkey].add_item(worry_score)

top_items_processed = [m.processed_items for m in monkeys]
top_items_processed.sort()
print(top_items_processed[-2] * top_items_processed[-1])
