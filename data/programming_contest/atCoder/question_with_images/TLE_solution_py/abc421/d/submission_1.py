Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())
S = {}
A = {}
for i in range(1, M+1):
    S[i], A[i] = input().split()
T = {}
B = {}
for i in range(1, L+1):
    T[i], B[i] = input().split()

Takahashi = [Rt, Ct]
Aoki = [Ra, Ca]

def move(pos, s):
    if s == 'U':
        pos[0] -= 1
    elif s == 'D':
        pos[0] += 1
    elif s == 'L':
        pos[1] -= 1
    elif s == 'R':
        pos[1] += 1
    return pos

for i in range(1, M+1):
    for _ in range(int(A[i])-1):

        keys = list(S.keys())

        insert_pos = keys.index(i) + 1

        new_key = max(keys) + 1

        for k in reversed(keys[insert_pos:]):
            S[k+1] = S[k]
        S[i+1] = S[i]

for i in range(1, L+1):
    for _ in range(int(B[i])-1):
        keys = list(T.keys())
        insert_pos = keys.index(i) + 1
        new_key = max(keys) + 1
        for k in reversed(keys[insert_pos:]):
            T[k+1] = T[k]
        T[i+1] = T[i]

ans = 0

for i in range(1, N+1):
    Takahashi = move(Takahashi, S[i])

    Aoki = move(Aoki, T[i])

    if Takahashi == Aoki:
        ans += 1

print(ans)