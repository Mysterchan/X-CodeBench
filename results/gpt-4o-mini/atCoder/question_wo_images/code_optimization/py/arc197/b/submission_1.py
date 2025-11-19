def solve():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    total = sum(A)
    max_score = 0
    
    for i in range(N):
        if A[i] > total / (i + 1):  # Check if current element is greater than average
            max_score += 1
            
    print(max_score)

T = int(input())
for _ in range(T):
    solve()