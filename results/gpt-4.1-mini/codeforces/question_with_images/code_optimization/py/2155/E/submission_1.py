import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    col_counts = [0] * m
    max_col = 0
    max_col_count = 0

    for __ in range(k):
        x, y = map(int, input().split())
        col_counts[y-1] += 1
        if y > max_col:
            max_col = y
            max_col_count = 1
        elif y == max_col:
            max_col_count += 1

    if max_col == 1:
        print("Yuyu")
        continue

    # If n == 1, only row 1 exists, so only tokens in column 1 and 2 matter
    if n == 1:
        # Only column 2 tokens can be moved to column 1
        if col_counts[1] % 2 == 1:
            print("Mimo")
        else:
            print("Yuyu")
        continue

    # For n > 1, check parity of tokens in columns 2..m
    # If any column from 2 to m has odd count, Mimo wins
    for count in col_counts[1:]:
        if count % 2 == 1:
            print("Mimo")
            break
    else:
        print("Yuyu")