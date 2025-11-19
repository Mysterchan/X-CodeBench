def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if all(a == 1 for a in A):
        print("Yes")
        return
    
    # Check the presence of at least one 1 and a sequence of zeros that can be manipulated
    if any(A[i] == 1 for i in range(N)):
        for i in range(N):
            if A[i] == 0 and A[(i + 1) % N] == 1 and A[(i + 2) % N] == 0:
                print("Yes")
                return
            if A[i] == 0 and A[(i - 1) % N] == 1 and A[(i - 2) % N] == 0:
                print("Yes")
                return

    print("No")

solve()