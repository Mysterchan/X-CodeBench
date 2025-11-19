def find_path(N, K):
    path = []
    # Количество возможных D и R в пути
    down_count = N - 1
    right_count = N - 1
    
    # Следить за числом выполняемых упражнений
    total_paths = 1
    for d in range(1, min(N, N) + 1):
        total_paths *= (down_count + right_count) // d
        total_paths //= d

    while down_count > 0 or right_count > 0:
        if down_count > 0:
            # Расчет количества путей, если мы выберем D
            num_paths_if_down = 1
            if down_count - 1 > 0 or right_count > 0:
                num_paths_if_down = 1
                for d in range(1, min(down_count, right_count) + 1):
                    num_paths_if_down *= (down_count + right_count - 1) // d
                    num_paths_if_down //= d

            if K <= num_paths_if_down:
                path.append('D')
                down_count -= 1
            else:
                path.append('R')
                K -= num_paths_if_down
                right_count -= 1
        else:
            path.append('R')
            right_count -= 1

    return ''.join(path)

N, K = map(int, input().split())
result = find_path(N, K)
print(result)