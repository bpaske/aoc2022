overlaps = 0
partial_overlaps = 0
with open("./input.txt") as f:
    for line in f:
        assignments = line.strip().split(",")
        bounds = [[int(b) for b in a.split("-")] for a in assignments]

        set1 = set(range(bounds[0][0], bounds[0][1] + 1))
        set2 = set(range(bounds[1][0], bounds[1][1] + 1))

        if set1.issuperset(set2) or set2.issuperset(set1):
            overlaps += 1

        if len(set1 & set2):
            partial_overlaps += 1
print(overlaps)
print(partial_overlaps)
