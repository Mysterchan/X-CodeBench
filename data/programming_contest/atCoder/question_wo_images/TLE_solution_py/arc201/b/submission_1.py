import sys
import threading

def main():
    import bisect
    from collections import defaultdict

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

        dp = {0: 0}

        for x in range(60):
            if not groups[x]:
                continue

            weight = 1 << x
            values = sorted(groups[x], reverse=True)

            prefix = [0]
            for v in values:
                prefix.append(prefix[-1] + v)

            new_dp = dict(dp)

            for take in range(1, len(values) + 1):
                w = take * weight
                v = prefix[take]

                for old_w, old_v in dp.items():
                    if old_w + w <= W:
                        new_val = old_v + v
                        if old_w + w not in new_dp or new_dp[old_w + w] < new_val:
                            new_dp[old_w + w] = new_val

            dp = new_dp

        results.append(str(max(dp.values())))

    print("\n".join(results))

threading.Thread(target=main).start()