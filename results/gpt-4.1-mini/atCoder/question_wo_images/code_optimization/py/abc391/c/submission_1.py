import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
pigeon = [i for i in range(1, N+1)]
nest = [1]*N
count_multi = 0  # number of nests with >= 2 pigeons

for _ in range(Q):
    query = input().split()
    ty = int(query[0])
    if ty == 1:
        P = int(query[1])
        H = int(query[2])
        old_nest = pigeon[P-1]
        # Remove pigeon from old nest
        old_count = nest[old_nest-1]
        nest[old_nest-1] = old_count - 1
        if old_count == 2:
            count_multi -= 1
        # Add pigeon to new nest
        new_count = nest[H-1]
        nest[H-1] = new_count + 1
        if new_count == 1:
            count_multi += 1
        pigeon[P-1] = H
    else:
        print(count_multi)