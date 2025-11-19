t = int(input())
for _ in range(t):
    s, k = map(int, input().split())
    # If Gleb never turns, he uses power k and moves k meters in one stroke.
    # If k == s, no turns needed, max power = k.
    # Otherwise, turning reduces power by 1 each time.
    # Gleb cannot turn immediately at start, must paddle first.
    # Also cannot turn twice in a row.
    #
    # The problem reduces to:
    # Find the maximum final power p (1 <= p <= k) such that Gleb can reach s
    # without leaving [0,s], starting at 0 with power k, and after some turns,
    # final power is p.
    #
    # Each turn reduces power by 1 (except if power=1, stays 1).
    #
    # The key insight:
    # The minimal distance Gleb can cover with final power p is:
    # sum of powers from p to k = (k + p)*(k - p + 1)//2
    #
    # Because Gleb can do a sequence of strokes forward and backward,
    # effectively covering the sum of powers from p to k.
    #
    # We want the minimal sum >= s to ensure Gleb can reach s with final power p.
    #
    # So we find the maximum p such that (k + p)*(k - p + 1)//2 >= s.
    #
    # We can binary search p in [1, k].
    
    left, right = 1, k
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        dist = (k + mid) * (k - mid + 1) // 2
        if dist >= s:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)