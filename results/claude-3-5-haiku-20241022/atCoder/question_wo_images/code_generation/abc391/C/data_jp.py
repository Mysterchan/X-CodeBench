N, Q = map(int, input().split())

# 各鳩がどの巣にいるかを記録
pigeon_location = list(range(N + 1))  # pigeon_location[i] = 鳩iがいる巣

# 各巣に何匹の鳩がいるかを記録
nest_count = [0] * (N + 1)
for i in range(1, N + 1):
    nest_count[i] = 1

# 複数の鳩がいる巣の個数
multiple_nests = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        P = query[1]
        H = query[2]
        
        # 現在鳩Pがいる巣
        current_nest = pigeon_location[P]
        
        # 現在の巣から鳩を移動
        if nest_count[current_nest] == 2:
            multiple_nests -= 1
        nest_count[current_nest] -= 1
        
        # 新しい巣に鳩を追加
        if nest_count[H] == 1:
            multiple_nests += 1
        nest_count[H] += 1
        
        # 鳩の位置を更新
        pigeon_location[P] = H
        
    else:  # query[0] == 2
        print(multiple_nests)