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

    # We want to maximize the number of times C2C can be held.
    # Each C2C requires:
    # - Div.1: one Hard and one Medium from the same writer
    # - Div.2: one Medium and one Easy from the same writer
    #
    # Each problem proposal can be used at most once.
    #
    # Let x_i = number of Div.1 sets from writer i
    # Let y_i = number of Div.2 sets from writer i
    #
    # Constraints per writer i:
    # x_i <= A_i (Hard)
    # x_i + y_i <= B_i (Medium)
    # y_i <= C_i (Easy)
    #
    # We want to maximize sum(x_i + y_i) over i.
    #
    # For each writer i, the maximum number of sets is limited by:
    # x_i <= A_i
    # y_i <= C_i
    # x_i + y_i <= B_i
    #
    # To maximize x_i + y_i, we want to find max x_i + y_i subject to above.
    #
    # For fixed i:
    # max x_i + y_i s.t.
    # x_i <= A_i
    # y_i <= C_i
    # x_i + y_i <= B_i
    #
    # The maximum sum is min(A_i + C_i, B_i)
    #
    # Because x_i + y_i <= B_i, and x_i <= A_i, y_i <= C_i,
    # the sum cannot exceed B_i, and also cannot exceed A_i + C_i.
    #
    # So max sets from writer i = min(A_i + C_i, B_i)
    #
    # The total maximum is sum over i of min(A_i + C_i, B_i).
    #
    # This is achievable by choosing:
    # x_i = min(A_i, B_i)
    # y_i = min(C_i, B_i - x_i)
    #
    # This respects all constraints and achieves the maximum sum.

    ans = 0
    for i in range(N):
        ans += min(A[i] + C[i], B[i])
    print(ans)