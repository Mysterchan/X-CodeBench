def min_length(A):
    B = A[:]
    changed = True
    while changed:
        changed = False
        i = 1
        while i < len(B) - 1:
            if B[i-1] ^ B[i+1] == B[i]:
                B.pop(i)
                changed = True
            else:
                i += 1
    return len(B)

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    i = int(input())
    A[i-1] = 1 - A[i-1]
    print(min_length(A))