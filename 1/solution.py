max_elf = None
current_load = 0
loads = [0,0,0]
with open ('./input.txt') as f:
    for line in f:
        l = line.strip()
        if l =='':
            if current_load > loads[0]:
                loads[0] = current_load
                loads.sort()
            current_load = 0
        else:
            current_load += int(l)

print(max(loads))
print(sum(loads))