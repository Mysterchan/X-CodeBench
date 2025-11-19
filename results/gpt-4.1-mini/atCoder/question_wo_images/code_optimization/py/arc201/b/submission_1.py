import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    MAX_X = 60

    for _ in range(T):
        N, W = map(int, input().split())
        groups = [[] for _ in range(MAX_X)]
        for __ in range(N):
            x, y = map(int, input().split())
            groups[x].append(y)

        # For each group, sort descending and compute prefix sums
        prefix_sums = []
        for x in range(MAX_X):
            if groups[x]:
                groups[x].sort(reverse=True)
                prefix = [0]
                for v in groups[x]:
                    prefix.append(prefix[-1] + v)
                prefix_sums.append((x, prefix))
            else:
                prefix_sums.append((x, [0]))

        # dp: list of (weight, value) pairs, sorted by weight, non-dominated
        dp = [(0, 0)]

        for x, prefix in prefix_sums:
            weight = 1 << x
            length = len(prefix) - 1  # number of items in this group

            # Generate candidates for this group: (weight, value)
            # candidates = [(take * weight, prefix[take]) for take in range(length + 1)]
            # We will merge dp and candidates efficiently

            new_dp = []
            i = 0  # pointer for dp
            j = 0  # pointer for candidates (take from 0 to length)

            # We'll merge dp and candidates by iterating over all combinations:
            # For each dp[i], we try all candidates[j], but that is O(len(dp)*length)
            # To optimize, we do a two-pointer merge exploiting sorted order

            # Instead, we do a merge of dp and candidates by iterating over candidates and dp in order
            # But since dp and candidates are sorted by weight, we can do a "knapsack-like" merge

            # We'll do a merge of dp and candidates by enumerating all combinations:
            # But to avoid O(len(dp)*length), we do a "merge" approach:
            # For each candidate weight w_c and value v_c, we merge with dp:
            # The combined weight = dp_w + w_c
            # The combined value = dp_v + v_c
            # We keep only those with weight <= W

            # To optimize, we do the following:
            # For each candidate (cw, cv), we merge with dp:
            # Since dp is sorted by weight, we can binary search max dp_w <= W - cw
            # But binary searching for each candidate is O(length * log(len(dp))) which is acceptable here.

            # So we precompute dp weights and values separately for binary search
            dp_weights = [w for w, v in dp]
            dp_values = [v for w, v in dp]

            from bisect import bisect_right

            candidates = [(take * weight, prefix[take]) for take in range(length + 1)]

            merged = []
            max_val = -1

            # For each candidate, find best dp to combine with
            for cw, cv in candidates:
                if cw > W:
                    continue
                rem = W - cw
                pos = bisect_right(dp_weights, rem) - 1
                if pos >= 0:
                    total_val = dp_values[pos] + cv
                    merged.append((cw + dp_weights[pos], total_val))

            # merged may have duplicates and unordered by weight, so sort and prune
            merged.sort()
            pruned = []
            max_v = -1
            for w_, v_ in merged:
                if v_ > max_v:
                    pruned.append((w_, v_))
                    max_v = v_

            dp = pruned

        # The answer is max value in dp
        ans = 0
        for w, v in dp:
            if w <= W and v > ans:
                ans = v
        print(ans)

threading.Thread(target=main).start()