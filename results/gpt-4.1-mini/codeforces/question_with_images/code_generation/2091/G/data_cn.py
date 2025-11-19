t = int(input())
for _ in range(t):
    s, k = map(int, input().split())
    # 若不轉身，力量保持 k，但可能無法剛好到達 s
    # 轉身 m 次，力量降為 max(k - m, 1)
    # 轉身 m 次，路徑長度為 k + (k-1) + (k-2) + ... + (k-m)
    # 但實際上，路徑長度 = (m+1)*k - m*(m+1)//2
    # 因為每次轉身力量減1，且每段移動力量依次為 k, k-1, ..., k-m
    # 我們要找最大 m，使得：
    # (m+1)*k - m*(m+1)//2 >= s 且 m <= k-1
    # 最終力量為 max(k - m, 1)
    # m最大為k-1，因為力量不會降到0
    
    left, right = 0, k - 1
    ans = 0
    while left <= right:
        m = (left + right) // 2
        dist = (m + 1) * k - m * (m + 1) // 2
        if dist >= s:
            ans = m
            right = m - 1
        else:
            left = m + 1
    # 最終力量
    power = k - ans
    if power < 1:
        power = 1
    print(power)