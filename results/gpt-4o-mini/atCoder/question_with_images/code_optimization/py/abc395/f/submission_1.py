import sys
input = sys.stdin.buffer.readline

def main():
    N, X = map(int, input().split())
    teeth = [tuple(map(int, input().split())) for _ in range(N)]

    # Using binary search to find the optimal H
    L, R = 0, 2 * 10**9 + 1

    while L < R:
        M = (L + R) // 2
        if all(M - X <= U + D <= M for U, D in teeth):
            R = M
        else:
            L = M + 1

    # The optimal H is L
    optimal_H = L
    total_cost = sum(U + D for U, D in teeth) - optimal_H * N

    print(total_cost)

if __name__ == "__main__":
    main()