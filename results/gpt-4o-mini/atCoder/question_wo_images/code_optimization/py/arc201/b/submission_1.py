import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0

    T = int(data[idx])
    idx += 1

    results = []

    for _ in range(T):
        N = int(data[idx])
        W = int(data[idx + 1])
        idx += 2

        groups = [[] for _ in range(60)]
        for _ in range(N):
            x = int(data[idx])
            y = int(data[idx + 1])
            idx += 2
            groups[x].append(y)

        dp = [0] * (W + 1)

        for x in range(60):
            if not groups[x]:
                continue

            weight = 1 << x
            values = sorted(groups[x], reverse=True)

            # Use a temporary list to avoid updating dp while iterating over it
            for j in range(W, weight - 1, -1):
                total_value = 0
                for k in range(len(values)):
                    total_value += values[k]
                    if j >= (k + 1) * weight:
                        dp[j] = max(dp[j], dp[j - (k + 1) * weight] + total_value)

        results.append(str(max(dp)))

    print("\n".join(results))

main()