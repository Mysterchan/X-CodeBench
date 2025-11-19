n = int(input())
a = list(map(int, input().split()))

# dp[i][j] = максимальная сумма после обработки первых i элементов, 
# когда в S осталось j элементов
# Инициализируем с -inf для невозможных состояний
INF = float('inf')
dp = [[-INF] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(i + 1):
        if dp[i][j] == -INF:
            continue
        
        # Операция 1: добавить a[i] в конец S
        if j + 1 <= n:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i])
        
        # Операция 2: удалить последний элемент из S (только если j > 0)
        if j > 0:
            dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j])

# Найти максимум среди всех возможных размеров S после n операций
ans = max(dp[n])
print(ans)