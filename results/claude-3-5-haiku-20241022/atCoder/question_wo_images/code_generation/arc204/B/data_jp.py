def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    
    # 各要素の現在位置と目標位置を記録
    size = N * K
    current_pos = [0] * (size + 1)
    for i in range(size):
        current_pos[P[i]] = i
    
    # サイクル分解を行う
    visited = [False] * (size + 1)
    cycles = []
    
    for start in range(1, size + 1):
        if visited[start]:
            continue
        
        cycle = []
        curr = start
        while not visited[curr]:
            visited[curr] = True
            cycle.append(curr)
            # 値currは位置curr-1にあるべき
            curr = P[current_pos[curr]]
        
        if len(cycle) > 1:
            cycles.append(cycle)
    
    total_points = 0
    
    for cycle in cycles:
        # サイクル内の各要素の現在位置を取得
        positions = [current_pos[val] for val in cycle]
        cycle_len = len(cycle)
        
        # サイクルをソートするには cycle_len - 1 回のスワップが必要
        # 各スワップでポイントを得られるかを貪欲に判断
        
        # 現在の位置配列を作成
        pos_map = {}
        for i, val in enumerate(cycle):
            pos_map[val] = positions[i]
        
        # サイクルを解消するためのスワップを選択
        # 貪欲法: できるだけNの倍数の距離でスワップ
        max_points = 0
        
        # DPまたは貪欲法でポイントを最大化
        # サイクルの長さが小さいので全探索的なアプローチも可能
        
        # より単純なアプローチ: 位置をグループ分け
        # 位置をN で割った商でグループ化
        groups = {}
        for i, val in enumerate(cycle):
            pos = positions[i]
            group = pos // N
            if group not in groups:
                groups[group] = []
            groups[group].append((pos, val))
        
        # 各グループ内でのスワップはポイントを得られる
        # グループ間のスワップは得られない
        
        # より正確な計算: サイクル内の要素をソートする際、
        # 同じグループ内でスワップできる回数を最大化
        
        # 簡易的アプローチ: 各要素について、目標位置との差がNの倍数かチェック
        for i, val in enumerate(cycle):
            target_pos = val - 1
            curr_pos = positions[i]
            if abs(target_pos - curr_pos) % N == 0 and target_pos != curr_pos:
                # このペアは直接スワップでポイント獲得可能
                pass
        
        # より精密な計算が必要
        # サイクルの構造から最大ポイントを計算
        
        # 位置を N で割った商（ブロック番号）を記録
        block_positions = [(positions[i] // N, i) for i in range(cycle_len)]
        target_blocks = [((val - 1) // N, i) for i, val in enumerate(cycle)]
        
        # 各値について、現在のブロックと目標ブロックが同じものをカウント
        same_block = 0
        for i in range(cycle_len):
            curr_block = positions[i] // N
            target_block = (cycle[i] - 1) // N
            if curr_block == target_block:
                same_block += 1
        
        # サイクル長 - 1 回のスワップのうち、最大で same_block - 1 回はポイント獲得可能
        # ただし、これは上限であり、実際はサイクルの構造に依存
        
        # より単純な計算: cycle_len - (異なるブロックの数)
        unique_blocks = len(set(positions[i] // N for i in range(cycle_len)))
        max_points += max(0, cycle_len - unique_blocks)
        
        total_points += max_points
    
    print(total_points)

solve()