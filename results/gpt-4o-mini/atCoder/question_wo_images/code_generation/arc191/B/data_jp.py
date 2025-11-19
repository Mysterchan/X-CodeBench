def find_good_numbers(N, K):
    good_numbers = []
    x = 1
    while len(good_numbers) < K:
        if (x ^ N) == (x % N):
            good_numbers.append(x)
        x += 1
    return good_numbers[K - 1] if len(good_numbers) >= K else -1

import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
results = []
for i in range(1, T + 1):
    N, K = map(int, data[i].split())
    result = find_good_numbers(N, K)
    results.append(result)

print('\n'.join(map(str, results)))