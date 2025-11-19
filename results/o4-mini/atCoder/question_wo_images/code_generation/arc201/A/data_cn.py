import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = [0]*N
    B = [0]*N
    C = [0]*N
    for i in range(N):
        a,b,c = map(int, input().split())
        A[i], B[i], C[i] = a,b,c

    # Div.1 from i-th author: min(A[i], B[i])
    # Div.2 from i-th author: min(B[i], C[i])
    # We want to maximize total Div.1 + Div.2, with the constraint that each B[i] is split between Div.1 and Div.2
    # Let x_i = number of Div.1 sets from i-th author
    # Then Div.2 sets from i-th author = min(B[i]-x_i, C[i])
    # x_i <= min(A[i], B[i])
    # x_i >= 0
    #
    # Maximize sum_i x_i + sum_i min(B[i]-x_i, C[i])
    #
    # For each i, define f_i(x_i) = x_i + min(B[i]-x_i, C[i])
    #
    # f_i(x_i) = 
    #   if B[i]-x_i <= C[i]: x_i + (B[i]-x_i) = B[i]
    #   else: x_i + C[i]
    #
    # So f_i(x_i) = min(B[i], x_i + C[i])
    #
    # Since x_i <= min(A[i], B[i]) = M_i
    #
    # f_i(x_i) is:
    # - increasing linearly with slope 1 until x_i + C[i] = B[i], i.e. x_i = B[i]-C[i]
    # - then constant B[i] for x_i >= B[i]-C[i]
    #
    # So to maximize f_i(x_i), pick x_i = max(M_i, B[i]-C[i]) if B[i]-C[i] <= M_i else M_i
    #
    # But we want to maximize sum f_i(x_i)
    #
    # Let's analyze:
    # If B[i] <= C[i], then B[i]-C[i] <= 0, so f_i(x_i) = B[i] for all x_i in [0, M_i]
    # So pick any x_i in [0, M_i], f_i(x_i) = B[i]
    #
    # If B[i] > C[i], then f_i(x_i) = x_i + C[i] for x_i < B[i]-C[i], and B[i] for x_i >= B[i]-C[i]
    # So to maximize f_i(x_i), pick x_i >= B[i]-C[i], but x_i <= M_i
    # So if M_i >= B[i]-C[i], pick x_i = M_i to get f_i(M_i) = min(B[i], M_i + C[i]) = B[i]
    # else pick x_i = M_i < B[i]-C[i], f_i(M_i) = M_i + C[i]
    #
    # So f_i(x_i) max = 
    #   if M_i >= B[i]-C[i]: B[i]
    #   else: M_i + C[i]
    #
    # So for each i:
    # max_f_i = B[i] if M_i >= B[i]-C[i] else M_i + C[i]
    #
    # sum max_f_i is the answer.

    ans = 0
    for i in range(N):
        M = min(A[i], B[i])
        diff = B[i] - C[i]
        if M >= diff:
            ans += B[i]
        else:
            ans += M + C[i]
    print(ans)