import os
import itertools


def is_right_order(first, second):
    if isinstance(first, int) and isinstance(second, int):
        return second - first
    elif isinstance(first, list) and isinstance(second, list):
        if first and second:
            cmp = is_right_order(first[0], second[0])
            if cmp == 0:
                return is_right_order(first[1:], second[1:])
            else:
                return cmp

        elif not first and not second:
            return 0
        elif first:
            return -1
        elif second:
            return 1
    elif isinstance(first, list):
        return is_right_order(first, [second])
    elif isinstance(second, list):
        return is_right_order([first], second)


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    right_order_indices_sum = 0
    for i, (first, second, _) in enumerate(itertools.zip_longest(f, f, f), 1):
        first_expression = eval(first)
        second_expression = eval(second)
        if is_right_order(first_expression, second_expression) >= 0:
            right_order_indices_sum += i

print(f"Part 1 answer: {right_order_indices_sum}")


class Expression(list):
    def __lt__(self, other):
        return is_right_order(self, other) < 0

    def __eq__(self, other):
        return is_right_order(self, other) == 0


with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
    expressions = [Expression([[2]]), Expression([[6]])]
    for i, (first, second, _) in enumerate(itertools.zip_longest(f, f, f), 1):
        expressions.append(Expression(eval(first)))
        expressions.append(Expression(eval(second)))

    expressions.sort(reverse=True)

    print(
        f"Part 2 answer: {(expressions.index([[6]]) + 1) * (expressions.index([[2]]) + 1)}"
    )
