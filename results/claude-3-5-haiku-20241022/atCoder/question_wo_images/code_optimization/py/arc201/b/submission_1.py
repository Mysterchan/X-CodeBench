import sys
import threading

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

        # Sort groups and compute prefix sums
        for x in range(60):
            if groups[x]:
                groups[x].sort(reverse=True)
                for i in range(1, len(groups[x])):
                    groups[x][i] += groups[x][i - 1]

        # Split into small and large weights
        threshold = 40
        small_groups = []
        large_items = []

        for x in range(threshold):
            if groups[x]:
                small_groups.append((x, groups[x]))

        for x in range(threshold, 60):
            if groups[x]:
                weight = 1 << x
                for i, val in enumerate(groups[x]):
                    large_items.append((weight * (i + 1), val))

        # DP for small weights
        dp = {0: 0}
        for x, values in small_groups:
            weight = 1 << x
            new_dp = dict(dp)
            for take in range(len(values)):
                w = (take + 1) * weight
                v = values[take]
                if w > W:
                    break
                for old_w, old_v in list(dp.items()):
                    new_w = old_w + w
                    if new_w <= W:
                        new_v = old_v + v
                        if new_w not in new_dp or new_dp[new_w] < new_v:
                            new_dp[new_w] = new_v
            dp = new_dp

        # Combine with large items
        max_val = max(dp.values()) if dp else 0

        if large_items:
            large_items.sort()
            for base_w, base_v in dp.items():
                remaining = W - base_w
                current_v = base_v
                for item_w, item_v in large_items:
                    if item_w <= remaining:
                        current_v = max(current_v, base_v + item_v)
                        remaining -= item_w
                    else:
                        break
                max_val = max(max_val, current_v)

        results.append(str(max_val))

    print("\n".join(results))

threading.Thread(target=main).start()