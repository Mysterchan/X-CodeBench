N = int(input())
A = list(map(int, input().split()))

B = [0] * N  # 最終的な石の数を格納する配列
remaining_stones = 0  # 祝いの石の合計数

for year in range(N-1, -1, -1):
    remaining_stones += A[year]  # 年ごとに持っている石を追加
    B[year] = remaining_stones  # 現在の宇宙人が祝われる石の数を記録
    if year > 0:
        remaining_stones -= 1  # 成人した宇宙人に1個ずつ石を渡す

print(' '.join(map(str, B)))