MOD = 998244353

n = int(input())
s = input()

def mat_mult(A, B):
    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
    return C

M0 = [
    [1, 1, 1],
    [1, 1, 1],
    [0, 0, 1]
]
M1 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 2]
]

M_total = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for c in s:
    if c == '0':
        M_current = M0
    else:
        M_current = M1
    M_total = mat_mult(M_current, M_total)

trace = (M_total[0][0] + M_total[1][1] + M_total[2][2]) % MOD
print((trace - 2 + MOD) % MOD)