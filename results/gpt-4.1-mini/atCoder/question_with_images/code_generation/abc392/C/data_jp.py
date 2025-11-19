import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Q_iはゼッケン番号iの人が着けている数
# P_iはi番目の人が見つめている人の番号
# i番目の人のゼッケン番号は何か分からないので、Qの逆引きを作る

# Qはゼッケン番号iの人の数なので、Q[i-1]がゼッケンiの人の数
# しかしi番目の人のゼッケン番号はわからない
# 問題文より、iはゼッケン番号なので、i番目の人はゼッケンiを着けている
# つまり、i番目の人のゼッケン番号はi
# なので、i番目の人が見つめている人はP[i-1]番目の人
# その人のゼッケン番号はP[i-1]
# その人の着けている数はQ[P[i-1]-1]

ans = [0]*N
for i in range(N):
    ans[i] = Q[P[i]-1]

print(*ans)