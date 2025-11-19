n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt_a = sum(x == -1 for x in a)
cnt_b = sum(x == -1 for x in b)

fixed_pairs = []
for x, y in zip(a, b):
    if x != -1 and y != -1:
        fixed_pairs.append(x + y)

# If no fixed pairs, always possible by choosing any non-negative integer sum
if not fixed_pairs:
    print("Yes")
    exit()

# The sum must be the same for all fixed pairs
target_sum = fixed_pairs[0]
for s in fixed_pairs:
    if s != target_sum:
        print("No")
        exit()

# Check if target_sum is at least max of fixed known elements (to keep A_i, B_i >= 0)
max_known = 0
for x, y in zip(a, b):
    if x != -1:
        max_known = max(max_known, x)
    if y != -1:
        max_known = max(max_known, y)

if target_sum < max_known:
    print("No")
    exit()

# For positions with one known and one unknown, check feasibility
for x, y in zip(a, b):
    if x == -1 and y != -1:
        # A_i = target_sum - y >= 0
        if target_sum < y:
            print("No")
            exit()
    elif x != -1 and y == -1:
        # B_i = target_sum - x >= 0
        if target_sum < x:
            print("No")
            exit()

print("Yes")