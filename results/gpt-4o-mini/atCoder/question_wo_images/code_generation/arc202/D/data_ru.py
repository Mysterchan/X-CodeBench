def count_king_sequences(H, W, T, A, B, C, D):
    MOD = 998244353

    # The distance the king needs to move in both the vertical and horizontal directions
    vertical_steps = abs(C - A)
    horizontal_steps = abs(D - B)

    # The total number of steps the king must take is T
    # Therefore, we need to determine if it's possible to reach the destination in exactly T moves
    if (vertical_steps + horizontal_steps) > T or (T - vertical_steps - horizontal_steps) % 2 != 0:
        return 0

    # Moves needed in the y-direction (vertical)
    y_moves = (T - vertical_steps) // 2 + vertical_steps
    x_moves = (T - horizontal_steps) // 2 + horizontal_steps

    # Function to compute factorial mod MOD
    def factorial(n):
        if n < 0:
            return 0
        f = 1
        for i in range(2, n + 1):
            f = (f * i) % MOD
        return f

    # Function to compute modular inverse using Fermat's little theorem
    def mod_inverse(a, p):
        return pow(a, p - 2, p)

    # Calculate combinations nCk under MOD
    def comb(n, k):
        if k < 0 or k > n:
            return 0
        return (factorial(n) * mod_inverse(factorial(k), MOD) % MOD * mod_inverse(factorial(n - k), MOD) % MOD) % MOD

    # The final answer we seek is the product of C(x_moves, T//2) * C(y_moves, T//2)
    answer = (comb(T, x_moves) * comb(T, y_moves)) % MOD
    
    return answer

# Read inputs
H, W, T, A, B, C, D = map(int, input().strip().split())
print(count_king_sequences(H, W, T, A, B, C, D))