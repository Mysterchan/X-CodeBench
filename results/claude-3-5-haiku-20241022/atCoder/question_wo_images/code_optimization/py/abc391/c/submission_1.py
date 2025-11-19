import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
pigeon_location = list(range(1, N+1))  # pigeon_location[i-1] = nest of pigeon i
nest_count = [1] * N  # nest_count[i-1] = number of pigeons in nest i
multi_pigeon_nests = 0  # count of nests with 2+ pigeons

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1], query[2]
        
        # Current nest of pigeon P
        old_nest = pigeon_location[P-1]
        
        # Update count for old nest
        if nest_count[old_nest-1] == 2:
            multi_pigeon_nests -= 1
        nest_count[old_nest-1] -= 1
        
        # Update count for new nest
        nest_count[H-1] += 1
        if nest_count[H-1] == 2:
            multi_pigeon_nests += 1
        
        # Update pigeon location
        pigeon_location[P-1] = H
    else:
        print(multi_pigeon_nests)