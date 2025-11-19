import sys
input = sys.stdin.readline

T = int(input())
# Since sum of N over all test cases <= 2*10^5, we can process all efficiently.

for _ in range(T):
    N, W = map(int, input().split())
    groups = [[] for __ in range(60)]
    for __ in range(N):
        X, Y = map(int, input().split())
        groups[X].append(Y)
    # For each group, sort descending by value
    for i in range(60):
        groups[i].sort(reverse=True)

    total_value = 0
    # For each bit from 0 to 59
    # We can pick at most W//(2^i) items from group i
    # So pick top min(len(groups[i]), W//(2^i)) items
    for i in range(60):
        weight = 1 << i
        max_count = W // weight
        if max_count == 0:
            continue
        take = min(len(groups[i]), max_count)
        if take > 0:
            total_value += sum(groups[i][:take])
    print(total_value)