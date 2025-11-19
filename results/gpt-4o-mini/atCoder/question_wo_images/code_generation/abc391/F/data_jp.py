import sys
import heapq

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
A = list(map(int, data[2:N + 2]))
B = list(map(int, data[N + 2:2 * N + 2]))
C = list(map(int, data[2 * N + 2:3 * N + 2]))

# 最大ヒープを使用するためのリスト
max_heap = []

# 各組み合わせの計算
for i in range(N):
    for j in range(N):
        # ここの計算結果を保持します
        B_j = B[j]
        term = A[i] * B_j
        for k in range(N):
            value = term + B_j * C[k] + C[k] * A[i]
            # ヒープに保存
            if len(max_heap) < K:
                heapq.heappush(max_heap, value)
            else:
                if value > max_heap[0]:
                    heapq.heappushpop(max_heap, value)

# K 番目に大きい値を取得する (min heap の root は K 番目に大きい値)
result = max_heap[0]
print(result)