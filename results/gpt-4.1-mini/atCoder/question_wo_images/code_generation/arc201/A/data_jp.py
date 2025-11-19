import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = [0]*N
    B = [0]*N
    C = [0]*N
    for i in range(N):
        a,b,c = map(int,input().split())
        A[i],B[i],C[i] = a,b,c

    # Div.1 requires (Hard, Medium) from same writer: min(A_i, B_i)
    # Div.2 requires (Medium, Easy) from same writer: min(B_i, C_i)
    # Each problem can be used at most once in one C2C (one Div.1 or Div.2)
    #
    # We want to maximize number of C2C held simultaneously.
    #
    # Let x_i = number of Div.1 contests from writer i
    # Let y_i = number of Div.2 contests from writer i
    #
    # Constraints per writer i:
    # x_i <= A_i
    # x_i <= B_i
    # y_i <= B_i
    # y_i <= C_i
    # Also, since B_i problems are shared between Div.1 and Div.2,
    # x_i + y_i <= B_i
    #
    # Objective: maximize sum_i (x_i + y_i)
    #
    # For each i, maximize x_i + y_i subject to:
    # x_i <= A_i
    # y_i <= C_i
    # x_i + y_i <= B_i
    #
    # The maximum x_i + y_i is min(A_i + C_i, B_i)
    #
    # Proof:
    # Since x_i <= A_i and y_i <= C_i,
    # x_i + y_i <= A_i + C_i
    # Also x_i + y_i <= B_i
    # So max x_i + y_i <= min(A_i + C_i, B_i)
    #
    # We can achieve this maximum by:
    # If A_i + C_i <= B_i:
    #   x_i = A_i, y_i = C_i
    # else:
    #   x_i = min(A_i, B_i)
    #   y_i = B_i - x_i (<= C_i guaranteed)
    #
    # So sum over i of min(A_i + C_i, B_i) is the answer.

    ans = 0
    for i in range(N):
        ans += min(A[i] + C[i], B[i])
    print(ans)