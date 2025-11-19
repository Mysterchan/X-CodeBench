def max_mirror_k(N, A):
    left = 0
    right = 0
    count = 0

    while left < N and right < N:
        if A[left] * 2 <= A[right]:
            count += 1
            left += 1
        right += 1
    
    return count

# 入力の読み込み
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))

# 結果の出力
print(max_mirror_k(N, A))