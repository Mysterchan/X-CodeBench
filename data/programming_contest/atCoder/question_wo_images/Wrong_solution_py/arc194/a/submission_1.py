def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[0]*2 for _ in range(n)]
    dp[0][1] = arr[0]
    dp[0][0] = arr[0]
    last_element = []
    if dp[0][1] >= dp[0][0]:
        last_element.append(arr[0])
    for i in range(1,n):
        if last_element:
            x = dp[i-1][0] - last_element[-1]
        else:
            x = float("-inf")
        y = dp[i-1][1] - arr[i-1]
        dp[i][0] = max(x,y)
        a =  dp[i-1][0] + arr[i]
        b = dp[i-1][1] + arr[i]
        dp[i][1] = max(a,b)
        if dp[i][1] > dp[i][0]:
            last_element.append(arr[i])
        else:
            if last_element:
                last_element.pop()
    ans = max(dp[n-1][1],dp[n-1][0])

    print(ans)
main()