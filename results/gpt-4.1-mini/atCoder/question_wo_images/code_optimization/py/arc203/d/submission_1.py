import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

s = sum(A)

# Precompute initial t and u
# t: count of positions i where (i==0 or A[i-1]==1) and A[i]==0
# u: count of positions i where t condition holds and (i==N-1 or A[i+1]==1)

def t_cond(i):
    return (i == 0 or A[i - 1] == 1) and A[i] == 0

def u_cond(i):
    return t_cond(i) and (i == N - 1 or A[i + 1] == 1)

t = 0
u = 0
for i in range(N):
    if t_cond(i):
        t += 1
        if u_cond(i):
            u += 1

for _ in range(Q):
    i = int(input()) - 1
    old = A[i]
    s -= old

    # Positions affected: i-1, i, i+1 (if in range)
    # For each, remove old contribution from t and u
    for pos in (i - 1, i, i + 1):
        if 0 <= pos < N:
            if t_cond(pos):
                t -= 1
                if u_cond(pos):
                    u -= 1

    # Flip A[i]
    A[i] ^= 1
    new = A[i]
    s += new

    # Add new contribution for affected positions
    for pos in (i - 1, i, i + 1):
        if 0 <= pos < N:
            if t_cond(pos):
                t += 1
                if u_cond(pos):
                    u += 1

    if s == N:
        ans = N
    elif s == 0:
        ans = 2
    elif u == t:
        ans = 2 + (A[0] == 0 and A[-1] == 0)
    else:
        ans = 3 * (t - u)
        if A[0] == 0 and A[1] == 1:
            ans += 1
        elif A[0] == 0:
            ans -= 1

        if A[-1] == 1:
            ans += 1
        elif A[-2] == 1 and A[-1] == 0:
            ans += 2

    print(ans)