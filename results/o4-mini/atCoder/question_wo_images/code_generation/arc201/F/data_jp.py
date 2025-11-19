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
        A[i] = A[i-1] + a
        B[i] = B[i-1] + b
        C[i] = C[i-1] + c
        D[i] = D[i-1] + d
        E[i] = E[i-1] + e

    # For each k, compute:
    # Div1 max = min(A_k, B_k, C_k)
    # Div2 max = min(B_k, C_k, D_k)
    # Div3 max = min(C_k, D_k, E_k)
    # We want to maximize x+y+z subject to:
    # x <= Div1 max
    # y <= Div2 max
    # z <= Div3 max
    # and the total usage of each problem type does not exceed the total available:
    # Hell: used only in Div1: x <= A_k
    # Hard: used in Div1 and Div2: x + y <= B_k
    # Medium: used in Div1, Div2, Div3: x + y + z <= C_k
    # Easy: used in Div2 and Div3: y + z <= D_k
    # Baby: used only in Div3: z <= E_k

    # The constraints are:
    # 0 <= x <= A_k
    # 0 <= y <= D_k (since y+z <= D_k and z>=0)
    # 0 <= z <= E_k
    # x + y <= B_k
    # x + y + z <= C_k
    # y + z <= D_k

    # We want to maximize x + y + z.

    # Approach:
    # For fixed k, try to find max x+y+z satisfying above.
    # Since x,y,z >=0 and integer (actually can be real since counts are large),
    # we can try to find max total = t.

    # Because constraints are linear, we can solve as follows:

    # For given k:
    # Let:
    # A = A[k], B = B[k], C = C[k], D = D[k], E = E[k]

    # We want max t = x + y + z
    # subject to:
    # x <= A
    # z <= E
    # y + z <= D
    # x + y <= B
    # x + y + z <= C

    # From y + z <= D => y <= D - z
    # From x + y <= B => y <= B - x
    # So y <= min(D - z, B - x)
    # Also y >= 0

    # Also x,y,z >= 0

    # Since t = x + y + z, and y <= min(D - z, B - x), y >=0,
    # y can be at most min(D - z, B - x), so:
    # t = x + y + z <= x + min(D - z, B - x) + z

    # To maximize t, we want to maximize x + y + z.

    # Let's try to fix z, then find max x,y.

    # For fixed z (0 <= z <= E):
    # y <= D - z
    # y <= B - x
    # y >= 0
    # x <= A
    # x >= 0

    # So y <= min(D - z, B - x)

    # To maximize x + y + z = z + x + y,
    # for fixed z, maximize x + y.

    # For fixed z, max x + y = max over x in [0,A] of x + min(D - z, B - x)

    # Since min(D - z, B - x) is decreasing in x (because B - x decreases as x increases),
    # the function f(x) = x + min(D - z, B - x) is piecewise linear.

    # Let's analyze:

    # Case 1: D - z <= B - x
    # Then min = D - z
    # f(x) = x + D - z = x + const, increasing in x
    # max at x = A, f(A) = A + D - z

    # Case 2: D - z > B - x
    # min = B - x
    # f(x) = x + B - x = B, constant

    # The boundary is at x = B - (D - z)

    # So for x <= B - (D - z), min = D - z, f(x) = x + D - z (increasing)
    # for x > B - (D - z), min = B - x, f(x) = B (constant)

    # So max f(x) = max of:
    # - f(B - (D - z)) = (B - (D - z)) + D - z = B
    # - f(A) = A + D - z

    # So max f(x) = max(B, A + D - z)

    # But x must be in [0,A], so B - (D - z) must be in [0,A] to consider that point.

    # If B - (D - z) < 0, then for all x in [0,A], min = B - x < D - z, so min = B - x,
    # f(x) = B constant, max f(x) = B

    # If B - (D - z) > A, then for all x in [0,A], min = D - z,
    # f(x) = x + D - z, max at x=A: A + D - z

    # So max f(x) = max(B, A + D - z)

    # Therefore, for fixed z:
    # max x + y = max(B, A + D - z)

    # But y >= 0, so min(D - z, B - x) >= 0 must hold.

    # Since y <= min(D - z, B - x), y >= 0, so min(D - z, B - x) >= 0.

    # For feasibility, D - z >= 0 and B - x >= 0.

    # Since x in [0,A], B - x >= B - A.

    # So min(D - z, B - A) >= 0 for y >= 0.

    # Since we want to maximize total t = x + y + z = z + max x + y = z + max(B, A + D - z)

    # So t(z) = z + max(B, A + D - z) = max(z + B, z + A + D - z) = max(z + B, A + D)

    # Since z + B is increasing in z, and A + D is constant.

    # For z in [0,E]:

    # If z + B <= A + D, then t(z) = A + D

    # Else t(z) = z + B

    # So t(z) = max(A + D, z + B)

    # To maximize t(z) over z in [0,E]:

    # If B + E <= A + D, then max t = A + D

    # Else max t = B + E

    # But also t <= C (since x + y + z <= C)

    # So final answer for each k is min(C, max(A + D, B + E))

    # Let's verify constraints:

    # x <= A

    # y + z <= D

    # x + y <= B

    # x + y + z <= C

    # z <= E

    # So the maximum total number of contests is min(C, max(A + D, B + E))

    # But we must also consider that x,y,z >= 0 and y <= min(D - z, B - x)

    # The above formula is consistent with constraints.

    # So for each k:

    # X_k = min(C_k, max(A_k + D_k, B_k + E_k))

    res = []
    for i in range(1, N+1):
        a,b,c,d,e = A[i], B[i], C[i], D[i], E[i]
        val = max(a + d, b + e)
        val = val if val <= c else c
        res.append(str(val))
    print(" ".join(res))