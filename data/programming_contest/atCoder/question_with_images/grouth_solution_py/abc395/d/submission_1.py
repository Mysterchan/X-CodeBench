N, Q = map(int, input().split())

bird_to_index = {}
index_to_su = {}
su_to_index = {}
for i in range(1, N + 1):
    bird_to_index[i] = i
    index_to_su[i] = i
    su_to_index[i] = i

for _ in range(Q):
    op = tuple(map(int, input().split()))
    if op[0] == 1:
        a, b = op[1], op[2]
        next_index = su_to_index[b]
        bird_to_index[a] = next_index
    elif op[0] == 2:
        a, b = op[1], op[2]
        a_index_now = su_to_index[a]
        b_index_now = su_to_index[b]
        index_to_su[a_index_now] = b
        index_to_su[b_index_now] = a
        su_to_index[a] = b_index_now
        su_to_index[b] = a_index_now
    else:
        now_index = bird_to_index[op[1]]
        print(index_to_su[now_index])