import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    U = list(map(int, input().split()))
    D = list(map(int, input().split()))
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))

    # The problem reduces to pairing good cells to cover the entire board.
    # Each operation colors a rectangle defined by two good cells.
    # The minimal total cost is the sum of all good cells' values,
    # because each good cell must be chosen exactly once (since each operation uses two distinct good cells never chosen before).
    # There are 4*(N-2) good cells, and each operation uses 2 good cells,
    # so total operations = 2*(N-2).
    # The minimal cost is sum of all good cells.

    total_cost = sum(U) + sum(D) + sum(L) + sum(R)
    print(total_cost)