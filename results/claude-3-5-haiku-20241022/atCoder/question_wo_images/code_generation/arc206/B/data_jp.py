def solve():
    N = int(input())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    # 位置iのスライムが最終的にどの位置に行くべきか
    target = [0] * N
    for i in range(N):
        target[i] = P[i] - 1
    
    # 逆置換: 値vが現在どの位置にあるか
    pos = [0] * N
    for i in range(N):
        pos[P[i] - 1] = i
    
    # 各サイクルを検出
    visited = [False] * N
    total_cost = 0
    
    for start in range(N):
        if visited[start]:
            continue
        
        # サイクルを構築
        cycle = []
        cur = start
        while not visited[cur]:
            visited[cur] = True
            cycle.append(cur)
            cur = target[cur]
        
        if len(cycle) == 1:
            continue
        
        # サイクル内の色のコストを集計
        colors = {}
        for idx in cycle:
            color = C[idx]
            if color not in colors:
                colors[color] = 0
            colors[color] += 1
        
        # 最も多い色を残し、他を変更
        max_count = max(colors.values())
        cycle_cost = sum(colors.keys()) * len(cycle) - sum(c * cnt for c, cnt in colors.items()) - max(colors.keys()) * max_count
        
        # より効率的な方法: 全体コストから最大頻度色のコストを引く
        total_color_sum = sum(C[idx] for idx in cycle)
        
        # 最適化: 最も頻度が高く、かつコストが高い色を残す
        # 各色について、その色を残した場合のコスト
        min_cost = float('inf')
        for keep_color, keep_count in colors.items():
            # keep_colorを残す場合、他の色を全てkeep_colorに変える
            cost = total_color_sum - keep_color * keep_count
            min_cost = min(min_cost, cost)
        
        total_cost += min_cost
    
    print(total_cost)

solve()