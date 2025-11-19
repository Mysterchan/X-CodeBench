import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()

# 找出所有1的位置
ones = [i for i, ch in enumerate(S) if ch == '1']
k = len(ones)

# 若只有一個1，已經連續，操作數為0
if k == 1:
    print(0)
    exit()

# 將1的位置轉換為相對位置，減去索引
# 目標是將所有1聚集在一起，且相對間距不變
# 這樣的最小移動次數是將所有1的位置移動到一段連續區間
# 使得移動距離總和最小
# 這個問題等價於將ones移動，使得它們的中位數位置對齊
# 計算移動距離時，使用 ones[i] - i，因為目標是連續的區間

pos = [ones[i] - i for i in range(k)]
pos.sort()
median = pos[k // 2]

# 計算總移動距離
res = sum(abs(x - median) for x in pos)
print(res)