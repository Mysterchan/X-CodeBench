MOD = 998244353

H, W = map(int, input().split())

# dp[i][j] = число матриц с максимальной достижимой позицией (i, j)
# Считаем число способов достичь каждой ячейки
total_matrices = pow(2, H + W, MOD)

result = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        # Ячейка (i,j) равна 1 если ri >= j или cj >= i
        # Число матриц где (i,j) = 1
        count = total_matrices - pow(2, i - 1 + j - 1, MOD)
        result = (result + count) % MOD

print(result)