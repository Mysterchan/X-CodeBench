import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

n, q = map(int, data[0].split())
pigeon_nest = list(range(1, n + 1))  # pigeon n starts in nest n
nest_count = [1] * (n + 1)  # number of pigeons in each nest, indexed by nest number
multiple_count = 0  # number of nests with more than one pigeon

def update_multiple_count(nest_index):
    global multiple_count
    if nest_count[nest_index] == 1:
        multiple_count += 1
    elif nest_count[nest_index] == 2:
        multiple_count -= 1

output = []

for line in data[1:q + 1]:
    parts = list(map(int, line.split()))
    
    if parts[0] == 2:
        output.append(multiple_count)
    else:
        p, h = parts[1], parts[2]
        current_nest = pigeon_nest[p - 1]
        
        # Move pigeon from current_nest to h
        # Update current nest
        nest_count[current_nest] -= 1
        update_multiple_count(current_nest)
        
        # Move pigeon to new nest
        pigeon_nest[p - 1] = h
        nest_count[h] += 1
        update_multiple_count(h)

print('\n'.join(map(str, output)))