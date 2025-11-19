import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # dp[i][j] - максимальный счет для многоугольника с вершинами от i до j по часовой стрелке (i < j)
    # Индексы по модулю n, но для удобства развернем массив в 2*n и будем работать с отрезками длины <= n
    # Решение - классическая задача о максимальной триангуляции правильного многоугольника с весами на вершинах
    # Формула перехода:
    # dp[i][j] = max(dp[i][k] + dp[k][j] + a[i]*a[k]*a[j]) для i < k < j

    # Для удобства удвоим массив, чтобы не заморачиваться с циклическими индексами
    a = a + a
    dp = [[0]*(2*n) for _ in range(2*n)]

    # Рассматриваем все отрезки длины >= 3
    for length in range(3, n+1):
        for i in range(0, 2*n - length + 1):
            j = i + length - 1
            best = 0
            for k in range(i+1, j):
                val = dp[i][k] + dp[k][j] + a[i]*a[k]*a[j]
                if val > best:
                    best = val
            dp[i][j] = best

    # Ответ - максимум dp[i][i+n-1] для i от 0 до n-1 (т.к. многоугольник цикличен)
    ans = 0
    for i in range(n):
        if dp[i][i+n-1] > ans:
            ans = dp[i][i+n-1]

    print(ans)