N = int(input())
A = list(map(int, input().split()))

# 0が含まれているかどうかをチェック
if all(a == 1 for a in A):
    print("Yes")
    exit()

# 0の位置をリストに格納
zero_positions = [i for i in range(N) if A[i] == 0]

# 0が隣接しているか、またはサイクルで隣接しているかをチェック
for i in range(len(zero_positions)):
    next_index = (i + 1) % len(zero_positions)
    if (zero_positions[next_index] - zero_positions[i]) % N == 1:
        print("No")
        exit()

print("Yes")