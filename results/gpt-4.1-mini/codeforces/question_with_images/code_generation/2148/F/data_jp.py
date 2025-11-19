import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arrays = []
    max_len = 0
    for __ in range(n):
        line = list(map(int, input().split()))
        k = line[0]
        arr = line[1:]
        arrays.append(arr)
        if k > max_len:
            max_len = k

    # bottom row length = max_len
    # For each column i (0-based), the bottom element after gravity is the minimal element
    # among all arrays that have length > i, because we can arrange arrays so that
    # the minimal element at position i falls to the bottom.
    # So bottom[i] = min(arr[j][i] for all j with len(arr[j]) > i)

    bottom = []
    for i in range(max_len):
        col_min = 2_10**5 + 1
        for arr in arrays:
            if len(arr) > i:
                if arr[i] < col_min:
                    col_min = arr[i]
        bottom.append(col_min)

    print(*bottom)