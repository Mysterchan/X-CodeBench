def max_perfect_records(T, cases):
    results = []
    for n, m in cases:
        max_perfect_players = min(n - 1, n * m // 2)
        results.append(max_perfect_players)
    return results

import sys
input = sys.stdin.read
data = input().splitlines()
T = int(data[0])
cases = [tuple(map(int, line.split())) for line in data[1:T+1]]
results = max_perfect_records(T, cases)
print('\n'.join(map(str, results)))