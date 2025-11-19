import sys
input = sys.stdin.readline

def main():
    N, X = map(int, input().split())
    U = [0]*N
    D = [0]*N
    for i in range(N):
        u, d = map(int, input().split())
        U[i], D[i] = u, d

    # The sum H = U_i + D_i must be the same for all i after grinding.
    # We want to find the maximum H such that:
    # 1) H <= U_i + D_i for all i (can't increase lengths)
    # 2) There exists a sequence u_i (0 <= u_i <= U_i) with |u_i - u_{i+1}| <= X and u_i + d_i = H
    # => u_i = H - d_i
    # So |(H - d_i) - (H - d_{i+1})| = |d_{i+1} - d_i| <= X must hold for all i.
    # But we can grind teeth, so we can reduce u_i and d_i.
    # The problem reduces to checking if there exists u_i in [0, U_i] with |u_i - u_{i+1}| <= X and u_i + d_i = H.
    # Since u_i = H - d_i, we need to check if for all i, 0 <= H - d_i <= U_i and |(H - d_i) - (H - d_{i+1})| <= X.
    # The difference condition becomes |d_{i+1} - d_i| <= X, which is fixed.
    # But since we can grind teeth, we can reduce lengths to satisfy the difference condition.
    # So we need to find the maximum H such that there exists u_i in [0, U_i] with |u_i - u_{i+1}| <= X and u_i + d_i = H.

    # We'll binary search on H.
    # For each H, we check if there exists u_i in [0, U_i] with u_i + d_i = H and |u_i - u_{i+1}| <= X.
    # This is equivalent to checking if intervals for u_i overlap with the difference constraints.

    # We'll maintain intervals [low_i, high_i] for u_i.
    # Initially, low_i = max(0, H - d_i), high_i = min(U_i, H - d_i)
    # But since u_i = H - d_i, low_i = high_i = H - d_i
    # So we just need to check if 0 <= H - d_i <= U_i for all i.
    # Then check if |(H - d_i) - (H - d_{i+1})| <= X for all i.
    # But since we can grind teeth, we can reduce u_i to satisfy difference constraints.
    # So we need to check if there exists a sequence u_i in [0, U_i] with |u_i - u_{i+1}| <= X and u_i + d_i = H.

    # We'll do a two-pass approach to find feasible intervals for u_i:
    # Forward pass: u_i >= max(u_{i-1} - X, 0)
    # Backward pass: u_i <= min(u_{i+1} + X, U_i)
    # Also u_i = H - d_i, so u_i must be in [0, U_i] and equal to H - d_i.

    # So for each i, u_i = H - d_i must be in [0, U_i].
    # We'll check if the sequence u_i = H - d_i can be adjusted to satisfy |u_i - u_{i+1}| <= X by grinding.

    # We'll implement a check function that tries to find feasible u_i intervals.

    def check(H):
        # Check if H - d_i in [0, U_i] for all i
        for i in range(N):
            val = H - D[i]
            if val < 0 or val > U[i]:
                return False

        # Forward pass: ensure u_i >= u_{i-1} - X
        low = [0]*N
        low[0] = H - D[0]
        for i in range(1, N):
            low[i] = max(H - D[i], low[i-1] - X)
            if low[i] > U[i]:
                return False

        # Backward pass: ensure u_i <= u_{i+1} + X
        high = [0]*N
        high[-1] = H - D[-1]
        for i in range(N-2, -1, -1):
            high[i] = min(H - D[i], high[i+1] + X)
            if high[i] < low[i]:
                return False

        return True

    left = 0
    right = min(U[i] + D[i] for i in range(N)) + 1

    while left + 1 < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid
        else:
            right = mid

    total = sum(U[i] + D[i] for i in range(N))
    print(total - left * N)

if __name__ == "__main__":
    main()