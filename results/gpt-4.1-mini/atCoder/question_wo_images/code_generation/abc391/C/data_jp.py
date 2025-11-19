import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
# 鳩iがいる巣
pigeon_pos = list(range(N+1))  # 1-indexed, pigeon_pos[i] = i 初期状態

# 各巣の鳩の数
nest_count = [0]*(N+1)
for i in range(1, N+1):
    nest_count[i] = 1

# 複数の鳩がいる巣の数
multi_nest = 0

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        _, P, H = query
        P = int(P)
        H = int(H)
        old_nest = pigeon_pos[P]

        # 移動前の巣のカウント更新
        c = nest_count[old_nest]
        if c == 2:
            multi_nest -= 1
        nest_count[old_nest] -= 1

        # 移動先の巣のカウント更新
        c = nest_count[H]
        nest_count[H] += 1
        if c == 1:
            multi_nest += 1

        pigeon_pos[P] = H

    else:
        # query[0] == '2'
        print(multi_nest)