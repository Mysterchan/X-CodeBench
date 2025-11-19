MOD = 998244353

def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[i][j][c] = число способов после выполнения i операций,
    # где j элементов в очереди, и текущее значение C равно c
    # Но C может быть очень большим, поэтому нам нужен другой подход
    
    # Используем dp[операция][размер_очереди][значение_C]
    # Но значение C может быть большим, поэтому отслеживаем возможные значения
    
    max_c = sum(B) + 1
    
    # dp[step][queue_size] = словарь {c: count}
    dp = [[{} for _ in range(N + 1)] for _ in range(2 * N + 1)]
    dp[0][0][0] = 1
    
    for step in range(2 * N):
        for queue_size in range(N + 1):
            if not dp[step][queue_size]:
                continue
            
            for c, count in dp[step][queue_size].items():
                # Действие 1: добавить элемент в очередь
                i = step - queue_size + 1  # текущий индекс для вставки
                if i <= N:
                    new_c = max(0, c - A[i - 1])
                    new_queue_size = queue_size + 1
                    if new_c not in dp[step + 1][new_queue_size]:
                        dp[step + 1][new_queue_size][new_c] = 0
                    dp[step + 1][new_queue_size][new_c] = (dp[step + 1][new_queue_size][new_c] + count) % MOD
                
                # Действие 2: удалить первый элемент из очереди
                if queue_size > 0:
                    # Первый элемент в очереди
                    # Элементы в очереди: от (step - queue_size + 1) до i
                    first_in_queue = step - queue_size + 1
                    new_c = c + B[first_in_queue - 1]
                    new_queue_size = queue_size - 1
                    if new_c not in dp[step + 1][new_queue_size]:
                        dp[step + 1][new_queue_size][new_c] = 0
                    dp[step + 1][new_queue_size][new_c] = (dp[step + 1][new_queue_size][new_c] + count) % MOD
    
    result = 0
    if dp[2 * N][0]:
        for c, count in dp[2 * N][0].items():
            if L <= c <= R:
                result = (result + count) % MOD
    
    print(result)

solve()