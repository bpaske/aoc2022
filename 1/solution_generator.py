import heapq
import itertools


def totals(filename):
    with open(filename) as f:
        while lines := list(itertools.takewhile(lambda x: x != "\n" and x != "", f)):
            yield sum(int(l.strip()) for l in lines)


three_largest = heapq.nlargest(3, totals("./input.txt"))
print(max(three_largest))
print(sum(three_largest))
