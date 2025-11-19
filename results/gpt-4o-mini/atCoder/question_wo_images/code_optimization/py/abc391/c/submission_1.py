import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
pigeon = list(range(1, N + 1))
nest_count = [1] * (N + 1)  # Count of pigeons in each nest (1-indexed)
multi_nests = 0  # Count of nests with more than one pigeon

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1], query[2]
        current_nest = pigeon[P - 1]
        
        # Move pigeon P from current_nest to H
        nest_count[current_nest] -= 1
        nest_count[H] += 1
        pigeon[P - 1] = H
        
        # Update multi_nests count
        if nest_count[current_nest] == 1:
            multi_nests -= 1
        elif nest_count[current_nest] == 2:
            multi_nests += 1
        
        if nest_count[H] == 2:
            multi_nests += 1
        elif nest_count[H] == 1:
            multi_nests -= 1
            
    elif query[0] == 2:
        print(multi_nests)