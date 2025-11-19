import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    A = [0]*n
    B = [0]*n
    C = [0]*n
    for i in range(n):
        a,b,c = map(int,input().split())
        A[i], B[i], C[i] = a,b,c

    # Binary search boundaries
    l, h = 0, 2_000_000_000_000_000  # 2*10^15, safe upper bound

    while h - l > 1:
        m = (l + h) // 2

        # Check feasibility for m times C2C
        # We want to check if we can assign m Div1 and m Div2 contests

        # For Div1: need m pairs of (Hard, Medium) from same writer
        # For Div2: need m pairs of (Medium, Easy) from same writer
        # Each problem proposal can be used at most once

        # The problem reduces to checking if there exists a way to split B[i] (Medium)
        # into two parts: used in Div1 and Div2, such that:
        # sum over i of min(A[i], B1[i]) >= m (Div1)
        # sum over i of min(B2[i], C[i]) >= m (Div2)
        # with B1[i] + B2[i] <= B[i]

        # The original code tries a heuristic:
        # First assign as many Div1 pairs as possible by min(B[i]-C[i], A[i]) (since B[i]-C[i] is the surplus medium after Div2)
        # Then assign remaining Div1 pairs from leftover A[i], B[i]
        # Then check if Div2 pairs sum to at least m

        # We can do the same but more efficiently without copying arrays multiple times.

        # We'll implement the same logic but avoid list copies and minimize operations.

        cnt1 = 0  # count of Div1 pairs assigned
        cnt2 = 0  # count of Div2 pairs assigned

        # First pass: assign Div1 pairs greedily from min(B[i]-C[i], A[i]) if positive
        # Because B[i]-C[i] is the medium problems not needed for Div2, so can be used for Div1
        # But if B[i]-C[i] < 0, no surplus medium for Div1 from that writer

        # We'll store leftover A[i], B[i] after this first assignment for second pass

        leftover_A = [0]*n
        leftover_B = [0]*n

        for i in range(n):
            surplus_medium = B[i] - C[i]
            if surplus_medium > 0:
                use = min(surplus_medium, A[i])
            else:
                use = 0
            cnt1 += use
            leftover_A[i] = A[i] - use
            leftover_B[i] = B[i] - use

        # Second pass: assign remaining Div1 pairs from leftover A[i], B[i]
        need = m - cnt1
        if need > 0:
            for i in range(n):
                if need == 0:
                    break
                use = min(need, leftover_A[i], leftover_B[i])
                cnt1 += use
                leftover_A[i] -= use
                leftover_B[i] -= use
                need -= use

        if cnt1 < m:
            h = m
            continue

        # Now assign Div2 pairs from leftover_B[i] and C[i]
        # leftover_B[i] is medium problems not used in Div1 second pass
        # C[i] is easy problems

        for i in range(n):
            cnt2 += min(leftover_B[i], C[i])

        if cnt2 >= m:
            l = m
        else:
            h = m

    print(l)