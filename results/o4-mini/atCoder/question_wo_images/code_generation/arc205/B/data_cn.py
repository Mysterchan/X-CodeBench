import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 讀取邊，但實際不需要存，因為答案只與N和M有關
for _ in range(M):
    input()

# 完全圖邊數
total_edges = N * (N - 1) // 2

# 最大黑邊數即為最大切割的邊數，為最大二分圖的邊數
# 將頂點分成兩組大小為 x 和 N-x，邊數為 x*(N-x)
# 最大值在 x = N//2 或 (N+1)//2
x = N // 2
max_black = max(x * (N - x), (x + 1) * (N - x - 1))

print(max_black)