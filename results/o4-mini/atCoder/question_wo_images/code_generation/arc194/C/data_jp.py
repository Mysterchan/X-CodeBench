def min_cost_to_match(N, A, B, C):
    total_cost = 0
    for i in range(N):
        if A[i] != B[i]:
            total_cost += C[i]
    return total_cost

# 入力の読み込み
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 最小コストの計算
result = min_cost_to_match(N, A, B, C)

# 結果の出力
print(result)