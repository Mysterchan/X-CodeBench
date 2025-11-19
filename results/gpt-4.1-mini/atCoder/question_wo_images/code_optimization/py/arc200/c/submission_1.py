import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    intervals = [tuple(map(int, input().split())) + (i,) for i in range(n)]
    # intervals: (L_i, R_i, original_index)

    # Sort intervals by L ascending
    intervals.sort(key=lambda x: x[0])

    ans = [0] * n
    stack = []

    # Assign seats from 1 to n in order of L ascending
    # Use a stack to maintain nested intervals
    for seat_num, (L, R, idx) in enumerate(intervals, 1):
        # Pop intervals that ended before current L
        while stack and stack[-1][1] < L:
            stack.pop()
        # Assign seat number
        ans[idx] = seat_num
        stack.append((L, R))

    print(*ans)