import sys
input = sys.stdin.readline

n = int(input())
chords = [tuple(sorted(map(int, input().split()))) for _ in range(n)]

# LIS helper function using binary search
def lis_length(seq):
    import bisect
    lis = []
    for x in seq:
        pos = bisect.bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)
        else:
            lis[pos] = x
    return len(lis)

# Sort chords by right endpoint ascending
chords.sort(key=lambda x: x[1])
right_end_sort_ans = [0] * (2 * n + 1)
info = []
ans = 0
for l, r in chords:
    # Find position to insert l in info (LIS on left endpoints)
    import bisect
    pos = bisect.bisect_left(info, l)
    if pos == len(info):
        info.append(l)
        ans += 1
    else:
        info[pos] = l
    right_end_sort_ans[r] = ans

# Sort chords by left endpoint descending
chords.sort(key=lambda x: x[0], reverse=True)
left_end_sort_ans = [0] * (2 * n + 1)
info = []
ans = 0
for l, r in chords:
    import bisect
    pos = bisect.bisect_left(info, r)
    if pos == len(info):
        info.append(r)
        ans += 1
    else:
        info[pos] = r
    left_end_sort_ans[l] = ans

# Prefix max for right_end_sort_ans
for i in range(1, 2 * n + 1):
    if right_end_sort_ans[i] < right_end_sort_ans[i - 1]:
        right_end_sort_ans[i] = right_end_sort_ans[i - 1]

# Suffix max for left_end_sort_ans
for i in range(2 * n - 1, 0, -1):
    if left_end_sort_ans[i] < left_end_sort_ans[i + 1]:
        left_end_sort_ans[i] = left_end_sort_ans[i + 1]

res = 0
for border in range(1, 2 * n + 1):
    if border == 2 * n:
        res = max(res, right_end_sort_ans[border])
    else:
        res = max(res, right_end_sort_ans[border] + left_end_sort_ans[border + 1])

print(res)