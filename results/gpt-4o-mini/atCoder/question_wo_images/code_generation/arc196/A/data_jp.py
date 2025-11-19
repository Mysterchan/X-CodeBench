def max_score(N, A):
    A.sort()
    score = 0
    for i in range(1, N):
        score += A[i] - A[i - 1]
    return score

# 入力の読み込み
N = int(input())
A = list(map(int, input().split()))

# 最大スコアの計算と出力
print(max_score(N, A))