N = int(input())
A = list(map(int, input().split()))

stones = A[:]

for year in range(1, N + 1):
    # year年後にyear-1番目の宇宙人(0-indexed)が成人する
    becoming_adult = year - 1
    
    # 石を1個以上持っている成人の数を数える
    gift_count = 0
    for j in range(becoming_adult):
        if stones[j] > 0:
            gift_count += 1
    
    # 成人する宇宙人に石を渡す
    for j in range(becoming_adult):
        if stones[j] > 0:
            stones[j] -= 1
    
    # 成人する宇宙人が石を受け取る
    stones[becoming_adult] += gift_count

print(' '.join(map(str, stones)))