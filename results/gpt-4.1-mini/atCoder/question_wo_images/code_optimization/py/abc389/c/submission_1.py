import sys
input = sys.stdin.readline

Q = int(input())
lengths = []
start = 0
offset = 0
total_length = 0

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        l = int(query[1])
        lengths.append(l)
        total_length += l
    elif t == 2:
        offset += lengths[start]
        start += 1
    else:
        k = int(query[1])
        # head coordinate = sum of lengths before that snake - offset
        # sum of lengths before snake at index start + k - 1 is total_length of first start+k-1 snakes
        # but we only have total_length of all snakes, so we maintain prefix sums implicitly by total_length and offset
        # Instead, we can keep track of prefix sums by maintaining total_length and offset, and start index
        # The head coordinate of snake at position start + k - 1 is sum of lengths of snakes before it minus offset
        # sum of lengths before snake at index i = total length of snakes from start to i-1
        # So we need prefix sums, but to avoid overhead, we can keep a prefix sums array

        # To optimize, we precompute prefix sums on the fly:
        # But since Q can be large, we can maintain prefix sums in a separate list

        # Let's maintain prefix sums of lengths for all snakes added
        # prefix_sums[i] = sum of lengths of snakes up to i-th (0-based)
        # So head coordinate of snake at index i = prefix_sums[i] - offset

        # We'll build prefix_sums incrementally

        # So let's implement prefix sums outside the loop

        pass

# Since we need prefix sums, let's rewrite with prefix sums

import sys
input = sys.stdin.readline

Q = int(input())
lengths = []
prefix_sums = [0]
start = 0
offset = 0

for _ in range(Q):
    query = input().split()
    t = int(query[0])
    if t == 1:
        l = int(query[1])
        lengths.append(l)
        prefix_sums.append(prefix_sums[-1] + l)
    elif t == 2:
        offset += lengths[start]
        start += 1
    else:
        k = int(query[1])
        idx = start + k - 1
        # head coordinate = prefix_sums[idx] - offset
        print(prefix_sums[idx] - offset)