import sys
input = sys.stdin.readline
inf = 1 << 60

def sub(N, A, B):
    # DP to cover all rows with pairs from A and B sequences
    dp = [[inf] * 3 for _ in range(3)]
    dp[0][0] = 0
    for i in range(1, N - 1):
        ndp = [[inf] * 3 for _ in range(3)]
        for j in range(3):
            for k in range(3):
                if j == 2 and k == 0:
                    # invalid state, skip
                    continue
                # keep old state
                ndp[j][k] = min(ndp[j][k], dp[j][k])
                # try to add from A
                if j + 1 < 3:
                    ndp[j + 1][k] = min(ndp[j + 1][k], dp[j][k] + A[i])
                # try to add from B
                if k + 1 < 3:
                    ndp[j][k + 1] = min(ndp[j][k + 1], dp[j][k] + B[i])
                # try to add both
                if j + 1 < 3 and k + 1 < 3:
                    ndp[j + 1][k + 1] = min(ndp[j + 1][k + 1], dp[j][k] + A[i] + B[i])
        dp = ndp
    return dp[2][2]

def calc(N, U, D, L, R):
    # We want to find minimal cost to cover all cells by pairing good cells
    # The problem reduces to choosing pairs of good cells to cover the board
    # The minimal cost is found by considering several patterns and DP

    # Sort each side by cost
    sU = sorted((U[i], i) for i in range(N))
    sD = sorted((D[i], i) for i in range(N))
    sL = sorted((L[i], i) for i in range(N))
    sR = sorted((R[i], i) for i in range(N))

    # Check if minimal pairs on U and D can be chosen without overlap
    # and similarly for L and R
    # If so, minimal cost is sum of two smallest on each side
    # Otherwise, fallback to sum of four smallest on all sides

    # Find minimal two on U and D
    mU1, posU1 = sU[0]
    mU2, posU2 = sU[1]
    mD1, posD1 = sD[0]
    mD2, posD2 = sD[1]
    mL1, posL1 = sL[0]
    mL2, posL2 = sL[1]
    mR1, posR1 = sR[0]
    mR2, posR2 = sR[1]

    ans0 = inf
    # Check if pairs on U and D can be chosen so that posU2 < posD1 and posR2 < posL1
    # This ensures no overlap in rows and columns
    if posU2 < posD1 and posR2 < posL1:
        ans0 = mU1 + mU2 + mD1 + mD2 + mL1 + mL2 + mR1 + mR2

    # Other candidates:
    # Add third minimal pairs on U and D
    ans1 = mU1 + mU2 + mD1 + mD2 + mL1 + mL2 + mR1 + mR2
    if N > 3:
        ans1 += sU[2][0] + sD[2][0]

    # Add third minimal pairs on L and R
    ans2 = mU1 + mU2 + mD1 + mD2 + mL1 + mL2 + mR1 + mR2
    if N > 3:
        ans2 += sL[2][0] + sR[2][0]

    # Use DP to cover rows with U and D, add minimal pairs on L and R
    ans3 = sub(N, U, D) + mL1 + mL2 + mR1 + mR2

    # Use DP to cover columns with R and L, add minimal pairs on U and D
    ans4 = sub(N, R, L) + mU1 + mU2 + mD1 + mD2

    return min(ans0, ans1, ans2, ans3, ans4)

T = int(input())
total_N = 0
for _ in range(T):
    N = int(input())
    total_N += N
    U = [inf] + list(map(int, input().split())) + [inf]
    D = [inf] + list(map(int, input().split())) + [inf]
    L = [inf] + list(map(int, input().split())) + [inf]
    R = [inf] + list(map(int, input().split())) + [inf]

    # Calculate answer for original and reversed sequences (to handle symmetry)
    ans1 = calc(N, U, D, L, R)
    ans2 = calc(N, U[::-1], D[::-1], L[::-1], R[::-1])
    print(min(ans1, ans2))