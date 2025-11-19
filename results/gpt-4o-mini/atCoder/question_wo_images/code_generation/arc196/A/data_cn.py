def max_score(N, A):
    A.sort()
    score = 0
    for i in range(1, N):
        score += A[i] - A[i - 1]
    return score

N = int(input())
A = list(map(int, input().split()))
print(max_score(N, A))