N = int(input())
A = list(map(int, input().split()))

# 计算总的操作次数
total_moves = sum(A)

# Fennec 先手，Snuke 后手
# 如果总的操作次数是奇数，Fennec 赢；如果是偶数，Snuke 赢
if total_moves % 2 == 1:
    print("Fennec")
else:
    print("Snuke")