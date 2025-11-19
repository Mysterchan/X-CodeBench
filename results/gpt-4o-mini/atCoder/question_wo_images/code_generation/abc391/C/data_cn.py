import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

# Read first line for N and Q
N, Q = map(int, data[0].split())

# Pigeon positions and a dictionary to count occupied nests
pigeon_positions = list(range(1, N + 1))  # Start with pigeon i in nest i
nest_count = defaultdict(int)  # To count pigeons in each nest
for i in range(1, N + 1):
    nest_count[i] = 1  # Initially, each nest has one pigeon

# Result list to gather output for type 2 queries
results = []

query_index = 1
for _ in range(Q):
    query = list(map(int, data[query_index].split()))
    if query[0] == 1:  # Move pigeon P to nest H
        P, H = query[1], query[2]
        current_nest = pigeon_positions[P - 1]  # Get current nest of pigeon P
        if current_nest != H:  # Move only if it's different
            # Update counts
            nest_count[current_nest] -= 1
            nest_count[H] += 1
            # Move pigeon position
            pigeon_positions[P - 1] = H
    else:  # query type 2
        # Count nests with more than one pigeon
        count = sum(1 for nests in nest_count.values() if nests > 1)
        results.append(str(count))
    
    query_index += 1

# Print all results for query type 2
print("\n".join(results))