def find_path(N, K):
    visits = [[0] * N for _ in range(N)]
    path = []

    down, right = 0, 0
    for _ in range(2 * N - 2):
        if down < N - 1 and (right == N - 1 or (visits[down + 1][right] < visits[down][right + 1]) or (visits[down + 1][right] == visits[down][right + 1])):
            path.append('D')
            down += 1
        else:
            path.append('R')
            right += 1
        visits[down][right] += 1

    for exercise in range(1, K):
        new_visits = [[0] * N for _ in range(N)]
        new_path = []
        down, right = 0, 0

        for _ in range(2 * N - 2):
            if down < N - 1 and (right == N - 1 or (visits[down + 1][right] < visits[down][right + 1]) or (visits[down + 1][right] == visits[down][right + 1])):
                new_path.append('D')
                down += 1
            else:
                new_path.append('R')
                right += 1
            new_visits[down][right] += 1
        
        visits = new_visits
        path = new_path
    
    return ''.join(path)


import sys
input = sys.stdin.read
N, K = map(int, input().split())
result = find_path(N, K)
print(result)