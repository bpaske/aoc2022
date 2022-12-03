total = 0
with open('./input.txt') as f:
    rucksack = 0
    for lines in zip(f, f, f):
        shared_items = set.intersection(*[set(l.strip()) for l in lines])
        for shared_item in shared_items:
            if shared_item.islower():
                total += ord(shared_item) - ord('a') + 1
            else:
                total += ord(shared_item) - ord('A') + 27

print(total)
