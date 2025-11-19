def max_probability(N, dice):
    from collections import defaultdict

    # 各サイコロの出目の出現頻度を記録する
    frequency = [defaultdict(int) for _ in range(N)]
    
    for i in range(N):
        K_i, *A_i = dice[i]
        for face in A_i:
            frequency[i][face] += 1

    max_prob = 0.0

    # 2つのサイコロを選んで確率を計算
    for i in range(N):
        for j in range(i + 1, N):
            # サイコロ i と j の出目の共通部分を見つける
            common_faces = set(frequency[i].keys()).intersection(set(frequency[j].keys()))
            if common_faces:
                prob = sum((frequency[i][face] / len(frequency[i])) * (frequency[j][face] / len(frequency[j])) for face in common_faces)
                max_prob = max(max_prob, prob)

    return max_prob

# 入力の読み込み
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
dice = [list(map(int, line.split())) for line in data[1:N + 1]]

# 最大確率を計算して出力
result = max_probability(N, dice)
print(f"{result:.12f}")