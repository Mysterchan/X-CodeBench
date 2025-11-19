def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(q):
        r, x = map(int, input().split())
        prefix = a[:r]

        filtered_prefix = [val for val in prefix if val <= x]

        if not filtered_prefix:
            print(0)
            continue

        dp = []
        for val in filtered_prefix:
            if not dp or val > dp[-1]:
                dp.append(val)
            else:
                l, h = 0, len(dp) - 1
                while l <= h:
                    mid = (l + h) // 2
                    if dp[mid] < val:
                        l = mid + 1
                    else:
                        h = mid - 1
                dp[l] = val
        print(len(dp))

solve()