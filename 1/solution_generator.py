import heapq

def totals(filename):
    with open (filename) as f:
        current_load = 0
        for line in f:
            l = line.strip()
            if l =='':
                yield current_load
                current_load = 0
            else:
                current_load += int(l)
three_largest = heapq.nlargest(3, totals('./input.txt'))
print(max(three_largest))
print(sum(three_largest))