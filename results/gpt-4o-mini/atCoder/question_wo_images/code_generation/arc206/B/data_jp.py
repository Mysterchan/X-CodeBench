def min_cost_to_good_sequence(N, P, C):
    # Pのインデックスを取得し、サイズの昇順に並べ替えたインデックスを得る
    sorted_indices = sorted(range(N), key=lambda i: P[i])
    
    # 色のコストを計算するための辞書を作成
    color_cost = {}
    
    # 現在の色を保持
    current_colors = [C[i] for i in sorted_indices]
    
    # 各色のコストを計算
    for i in range(N):
        color = current_colors[i]
        if color not in color_cost:
            color_cost[color] = 0
        color_cost[color] += C[sorted_indices[i]]
    
    # 最小コストを求める
    min_cost = float('inf')
    
    for color in color_cost:
        cost = 0
        for i in range(N):
            if current_colors[i] != color:
                cost += C[sorted_indices[i]]
        min_cost = min(min_cost, cost)
    
    return min_cost

# 入力の読み込み
N = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

# 結果の出力
print(min_cost_to_good_sequence(N, P, C))