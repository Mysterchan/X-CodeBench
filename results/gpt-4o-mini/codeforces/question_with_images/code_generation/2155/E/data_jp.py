def can_win(n, m, k, tokens):
    col_count = [0] * (m + 1)
    
    for x, y in tokens:
        col_count[y] += 1
    
    height = [0] * (m + 1)
    
    for j in range(1, m + 1):
        if col_count[j] > 0:
            height[j] = height[j - 1] + 1
        else:
            height[j] = height[j - 1]
    
    total_height = 0
    
    for j in range(m, 0, -1):
        if height[j] > 0:
            total_height += 1
    
    return "Mimo" if total_height % 2 == 1 else "Yuyu"

import sys
input = sys.stdin.readline

t = int(input())
results = []
for _ in range(t):
    n, m, k = map(int, input().split())
    tokens = [tuple(map(int, input().split())) for _ in range(k)]
    result = can_win(n, m, k, tokens)
    results.append(result)

print("\n".join(results))