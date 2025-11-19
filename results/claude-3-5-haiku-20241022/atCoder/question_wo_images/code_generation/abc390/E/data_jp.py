N, X = map(int, input().split())
foods = []
for _ in range(N):
    v, a, c = map(int, input().split())
    foods.append((v-1, a, c))

# ビタミン1, 2, 3ごとに食べ物を分類
vitamins = [[], [], []]
for v, a, c in foods:
    vitamins[v].append((a, c))

# 各ビタミンごとにカロリーあたりの効率でソート(降順)
for i in range(3):
    vitamins[i].sort(key=lambda x: -x[0]/x[1])

def get_max_vitamin(vit_list, calorie_budget):
    """与えられたカロリー予算で得られる最大ビタミン量"""
    if calorie_budget < 0:
        return 0
    # ナップサック問題
    dp = [0] * (calorie_budget + 1)
    for a, c in vit_list:
        for j in range(calorie_budget, c - 1, -1):
            dp[j] = max(dp[j], dp[j-c] + a)
    return dp[calorie_budget]

# ビタミン1とビタミン2の摂取量を全探索
max_result = 0

# ビタミン1の摂取パターンを全探索
v1_patterns = [(0, 0)]  # (ビタミン量, カロリー)
for a, c in vitamins[0]:
    new_patterns = []
    for va, vc in v1_patterns:
        if vc + c <= X:
            new_patterns.append((va + a, vc + c))
    v1_patterns.extend(new_patterns)

# ビタミン2の摂取パターンを全探索
v2_patterns = [(0, 0)]
for a, c in vitamins[1]:
    new_patterns = []
    for va, vc in v2_patterns:
        if vc + c <= X:
            new_patterns.append((va + a, vc + c))
    v2_patterns.extend(new_patterns)

# ビタミン1とビタミン2の組み合わせを探索
for v1_amount, v1_cal in v1_patterns:
    for v2_amount, v2_cal in v2_patterns:
        if v1_cal + v2_cal <= X:
            remaining_cal = X - v1_cal - v2_cal
            v3_amount = get_max_vitamin(vitamins[2], remaining_cal)
            min_vitamin = min(v1_amount, v2_amount, v3_amount)
            max_result = max(max_result, min_vitamin)

print(max_result)