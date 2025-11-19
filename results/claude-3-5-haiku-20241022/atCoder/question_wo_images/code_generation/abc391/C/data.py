N, Q = map(int, input().split())

# pigeon_location[i] = nest where pigeon i is located
pigeon_location = [0] + list(range(1, N + 1))  # pigeon i starts in nest i

# nest_count[i] = number of pigeons in nest i
nest_count = [0] + [1] * N  # nest i starts with 1 pigeon

# Count of nests with more than one pigeon
nests_with_multiple = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        P, H = query[1], query[2]
        
        # Find current nest of pigeon P
        old_nest = pigeon_location[P]
        
        # Update old nest
        if nest_count[old_nest] > 1:
            nests_with_multiple -= 1
        nest_count[old_nest] -= 1
        if nest_count[old_nest] > 1:
            nests_with_multiple += 1
        
        # Update new nest
        if nest_count[H] > 1:
            nests_with_multiple -= 1
        nest_count[H] += 1
        if nest_count[H] > 1:
            nests_with_multiple += 1
        
        # Update pigeon location
        pigeon_location[P] = H
        
    else:  # query[0] == 2
        print(nests_with_multiple)