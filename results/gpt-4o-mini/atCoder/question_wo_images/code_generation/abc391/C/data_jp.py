import sys
from collections import defaultdict

input = sys.stdin.read
data = input().splitlines()

# Read N and Q
N, Q = map(int, data[0].split())

# Initialize nests and a count of nests with multiple pigeons
nests = [0] * (N + 1)  # nests[i] means how many pigeons are in nest i
multi_count = 0  # count of nests with more than 1 pigeon
results = []

# Initially, each pigeon i is in nest i
for i in range(1, N + 1):
    nests[i] = 1

for i in range(1, Q + 1):
    query = list(map(int, data[i].split()))
    
    if query[0] == 1:
        P, H = query[1], query[2]
        
        current_nest = P  # since pigeon P starts in nest P
        if nests[current_nest] > 1:
            if nests[current_nest] == 2:
                multi_count -= 1

        nests[current_nest] -= 1
        if nests[current_nest] == 1:
            multi_count += 1
        
        nests[H] += 1
        if nests[H] == 2:
            multi_count += 1

    elif query[0] == 2:
        results.append(multi_count)

# Output all results for query type 2
print("\n".join(map(str, results)))