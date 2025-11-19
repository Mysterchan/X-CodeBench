import sys
import threading

def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    # Since sum of N over all tests <= 2*10^5, we can process all tests efficiently.

    for _ in range(T):
        N, W = map(int, input().split())
        # For each test, we will group items by their X_i (weight exponent)
        # For each group, sort items by descending Y_i and compute prefix sums.
        groups = [[] for __ in range(60)]
        for __ in range(N):
            X, Y = map(int, input().split())
            groups[X].append(Y)

        # For each group, sort descending and prefix sums
        prefix_sums = []
        for i in range(60):
            if groups[i]:
                groups[i].sort(reverse=True)
                ps = [0]
                for val in groups[i]:
                    ps.append(ps[-1] + val)
                prefix_sums.append((i, ps))
            else:
                prefix_sums.append((i, [0]))

        # We want to select k_i items from group i, total weight sum k_i * 2^i <= W
        # Maximize sum of prefix_sums[i][k_i]

        # Since weights are powers of two, and W can be large, we can try a greedy approach:
        # For each group, the max number of items we can take is min(len(groups[i]), W // 2^i)
        # We try to take as many as possible from groups with higher value per weight.

        # But value per weight varies per item, so we must consider items individually.

        # However, since weights are powers of two, and items grouped by weight,
        # and we want max sum of values with total weight <= W,
        # we can try a meet-in-the-middle or a heuristic.

        # But constraints are large, so meet-in-the-middle is impossible.

        # Alternative approach:
        # Since weights are powers of two, and W up to 10^18,
        # and sum of N is 2*10^5, we can try a binary search on answer or a DP.

        # DP is impossible due to large W.

        # Another approach:
        # For each group i:
        #   max_items = min(len(groups[i]), W // (1 << i))
        #   We can take up to max_items from this group.

        # So we can try to take max_items from each group, sum their values,
        # and check if total weight <= W.

        # But we want to maximize sum of values.

        # Since items are sorted descending in each group,
        # taking more items from groups with higher value per weight is better.

        # So we can try a greedy approach:
        # For each group, we can take from 0 to max_items items.
        # But how to decide how many items to take from each group?

        # Since weights differ by powers of two, and W is large,
        # we can try a heuristic:
        # For each group, take as many items as possible (up to max_items),
        # then if total weight > W, we try to remove items from groups with lowest value per weight.

        # But value per weight varies per item, so we need to consider items individually.

        # Alternative approach:
        # Since weights are powers of two, and items grouped by weight,
        # we can try to process groups from largest weight to smallest weight.

        # For each group i from 59 down to 0:
        #   max_items = min(len(groups[i]), W // (1 << i))
        #   take max_items items (top max_items values)
        #   subtract weight from W
        #   add values to answer

        # This greedy approach works because:
        # - Taking heavier items first uses up capacity quickly.
        # - But maybe smaller items have better value per weight.

        # So we should try to take items with best value per weight first.

        # Since weight is 2^X, value per weight = Y / 2^X

        # Let's create a list of all items with (value_per_weight, X, Y)
        # Sort descending by value_per_weight
        # Then pick items greedily until weight limit W is reached.

        items = []
        for i in range(60):
            w = 1 << i
            for val in groups[i]:
                items.append((val / w, w, val))
        items.sort(key=lambda x: x[0], reverse=True)

        total_value = 0
        total_weight = 0
        for vpw, w, val in items:
            if total_weight + w <= W:
                total_weight += w
                total_value += val
            # else skip

        print(total_value)

threading.Thread(target=main).start()