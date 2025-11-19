import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = [0]*(N+1)
    B = [0]*(N+1)
    C = [0]*(N+1)
    D = [0]*(N+1)
    E = [0]*(N+1)
    for i in range(1, N+1):
        a,b,c,d,e = map(int, input().split())
        A[i] = a
        B[i] = b
        C[i] = c
        D[i] = d
        E[i] = e

    res = []
    sumA = 0
    sumB = 0
    sumC = 0
    sumD = 0
    sumE = 0
    for i in range(1, N+1):
        sumA += A[i]
        sumB += B[i]
        sumC += C[i]
        sumD += D[i]
        sumE += E[i]

        # For each k, we want to find max X_k such that:
        # X_k <= sumA (for Div.1 hell)
        # X_k <= sumB (for Div.1 hard + Div.2 hard)
        # X_k <= sumC (for Div.1 medium + Div.2 medium + Div.3 medium)
        # X_k <= sumD (for Div.2 easy + Div.3 easy)
        # X_k <= sumE (for Div.3 baby)
        #
        # But each Div requires:
        # Div.1: 1 hell, 1 hard, 1 medium from same author
        # Div.2: 1 hard, 1 medium, 1 easy from same author
        # Div.3: 1 medium, 1 easy, 1 baby from same author
        #
        # Since each problem can be used only once, and Div.1, Div.2, Div.3 can be from different authors,
        # the total number of contests X_k is limited by the sum of these constraints.
        #
        # Let x,y,z be the number of Div.1, Div.2, Div.3 contests respectively.
        # Then:
        # x <= sumA
        # x + y <= sumB
        # x + y + z <= sumC
        # y + z <= sumD
        # z <= sumE
        #
        # We want to maximize x + y + z subject to above.
        #
        # From constraints:
        # x <= sumA
        # y <= sumB - x
        # z <= sumC - x - y
        # y + z <= sumD
        # z <= sumE
        #
        # To maximize x + y + z, try to use all sumA for x:
        # x = min(sumA, ...)
        #
        # Then y <= min(sumB - x, sumD - z)
        # z <= min(sumC - x - y, sumD - y, sumE)
        #
        # This is a linear optimization problem with 3 variables.
        #
        # We can solve it by iterating over possible x (from 0 to sumA),
        # but sumA can be large.
        #
        # Instead, we can use a direct formula:
        #
        # Since x + y + z = total
        # and constraints:
        # x <= sumA
        # y <= sumB - x
        # z <= sumE
        # y + z <= sumD
        # x + y + z <= sumC
        #
        # We want to maximize total = x + y + z
        #
        # For fixed x:
        # y + z <= sumD
        # y <= sumB - x
        # z <= sumE
        # x + y + z <= sumC
        #
        # So y + z <= min(sumD, sumC - x)
        # y <= sumB - x
        # z <= sumE
        #
        # To maximize y + z under y <= sumB - x, z <= sumE, y + z <= min(sumD, sumC - x)
        #
        # The maximum y + z is min(sumD, sumC - x, sumB - x + sumE)
        #
        # Because y + z <= sumD
        # y + z <= sumC - x
        # y + z <= (sumB - x) + sumE
        #
        # So max total = x + max_yz
        # max_yz = min(sumD, sumC - x, sumB - x + sumE)
        #
        # We want to find x in [0, sumA] that maximizes x + min(sumD, sumC - x, sumB - x + sumE)
        #
        # Let's define f(x) = x + min(sumD, sumC - x, sumB - x + sumE)
        #
        # f(x) = x + m(x)
        # where m(x) = min(sumD, sumC - x, sumB - x + sumE)
        #
        # m(x) is min of three linear functions:
        # sumD (constant)
        # sumC - x (decreasing in x)
        # sumB - x + sumE = (sumB + sumE) - x (decreasing in x)
        #
        # So m(x) = min(sumD, sumC - x, (sumB + sumE) - x)
        #
        # Since sumC - x and (sumB + sumE) - x are both decreasing in x,
        # and sumD is constant,
        # m(x) is piecewise linear.
        #
        # We can find the x where sumC - x = sumD => x = sumC - sumD
        # and where (sumB + sumE) - x = sumD => x = sumB + sumE - sumD
        #
        # Also where sumC - x = (sumB + sumE) - x => sumC = sumB + sumE
        #
        # We can check candidates at these points and boundaries 0 and sumA.
        #
        # We'll check f(x) at:
        # x = 0
        # x = sumA
        # x = sumC - sumD
        # x = sumB + sumE - sumD
        #
        # Only consider x in [0, sumA]
        #
        # Then take max f(x).
        #
        candidates = [0, sumA]
        if 0 <= sumC - sumD <= sumA:
            candidates.append(sumC - sumD)
        if 0 <= sumB + sumE - sumD <= sumA:
            candidates.append(sumB + sumE - sumD)

        def f(x):
            m = min(sumD, sumC - x, sumB + sumE - x)
            return x + m

        ans = 0
        for x in candidates:
            val = f(x)
            if val > ans:
                ans = val
        res.append(str(ans))
    print(' '.join(res))