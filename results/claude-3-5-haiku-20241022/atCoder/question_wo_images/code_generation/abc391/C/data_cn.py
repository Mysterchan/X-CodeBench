N, Q = map(int, input().split())

# pigeon_location[i] stores the nest where pigeon i is located
pigeon_location = [0] + list(range(1, N + 1))  # pigeon_location[i] = i initially

# nest_count[i] stores the number of pigeons in nest i
nest_count = [0] * (N + 1)
for i in range(1, N + 1):
    nest_count[i] = 1

# Count of nests with more than one pigeon
nests_with_multiple = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        P = query[1]
        H = query[2]
        
        # Get current nest of pigeon P
        current_nest = pigeon_location[P]
        
        # Remove pigeon P from current nest
        nest_count[current_nest] -= 1
        if nest_count[current_nest] == 1:
            nests_with_multiple -= 1
        
        # Add pigeon P to nest H
        nest_count[H] += 1
        if nest_count[H] == 2:
            nests_with_multiple += 1
        
        # Update pigeon location
        pigeon_location[P] = H
    
    else:  # query[0] == 2
        print(nests_with_multiple)