total = 0
with open('./input.txt') as f:
    for line in f:
        l = line.strip()
        half_length = len(l) //2
        shared_items = set(l[:half_length]) & set(l[half_length:])

        for shared_item in shared_items:
            if shared_item.islower():
                total += ord(shared_item) - ord('a') + 1
            else:
                total += ord(shared_item) - ord('A') + 27

print(total)
