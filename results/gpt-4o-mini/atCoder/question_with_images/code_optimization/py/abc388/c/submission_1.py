def solve(N, A):
    ans = 0
    j = 0
    for i in range(N):
        while j < N and A[j] < 2 * A[i]:
            j += 1
        ans += (N - j)
    return ans

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))