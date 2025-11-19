N = int(input())
A = list(map(int, input().split()))

s = sum(A)

def compute_t_u():
    t = 0
    u = 0
    for i in range(N):
        if A[i] == 0 and (i == 0 or A[i-1] == 1):
            t += 1
            if i == N-1 or A[i+1] == 1:
                u += 1
    return t, u

t, u = compute_t_u()

Q = int(input())
for _ in range(Q):
    i = int(input()) - 1
    
    # Update s
    s -= A[i]
    
    # Update t (before flip)
    if A[i] == 0 and (i == 0 or A[i-1] == 1):
        t -= 1
    if i < N-1 and A[i+1] == 0 and (i+1 == 0 or A[i] == 1):
        t -= 1
    
    # Update u (before flip)
    if i > 0 and A[i-1] == 0 and (i-1 == 0 or A[i-2] == 1) and A[i] == 1:
        u -= 1
    if A[i] == 0 and (i == 0 or A[i-1] == 1) and (i == N-1 or A[i+1] == 1):
        u -= 1
    if i < N-1 and A[i+1] == 0 and (i+1 == 0 or A[i] == 1) and (i+1 == N-1 or A[i+2] == 1):
        u -= 1
    
    # Flip
    A[i] ^= 1
    s += A[i]
    
    # Update t (after flip)
    if A[i] == 0 and (i == 0 or A[i-1] == 1):
        t += 1
    if i < N-1 and A[i+1] == 0 and (i+1 == 0 or A[i] == 1):
        t += 1
    
    # Update u (after flip)
    if i > 0 and A[i-1] == 0 and (i-1 == 0 or A[i-2] == 1) and A[i] == 1:
        u += 1
    if A[i] == 0 and (i == 0 or A[i-1] == 1) and (i == N-1 or A[i+1] == 1):
        u += 1
    if i < N-1 and A[i+1] == 0 and (i+1 == 0 or A[i] == 1) and (i+1 == N-1 or A[i+2] == 1):
        u += 1
    
    # Compute answer
    if s == N:
        ans = N
    elif s == 0:
        ans = max(2, s)
    elif u == t:
        ans = 2 + (1 if A[0] == 0 and A[-1] == 0 else 0)
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