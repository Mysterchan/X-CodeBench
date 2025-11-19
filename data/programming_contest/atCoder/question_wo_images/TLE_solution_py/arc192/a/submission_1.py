def solve():
    N = int(input())
    A = list(map(int, input().split()))

    def check(S):
        A_copy = A[:]
        changed = True
        while changed:
            changed = False
            for i in range(N):
                if S[i] == 'A' and S[(i + 1) % N] == 'R' and S[(i + 2) % N] == 'C' and A_copy[i] == 0:
                    A_copy[i] = 1
                    A_copy[(i + 1) % N] = 1
                    changed = True
                if S[(i + 2) % N] == 'A' and S[(i + 1) % N] == 'R' and S[i] == 'C' and A_copy[i] == 0:
                    A_copy[i] = 1
                    A_copy[(i + 1) % N] = 1
                    changed = True
        return all(a == 1 for a in A_copy)

    import itertools
    for S in itertools.product('ARC', repeat=N):
        if check(S):
            print("Yes")
            return
    print("No")

solve()