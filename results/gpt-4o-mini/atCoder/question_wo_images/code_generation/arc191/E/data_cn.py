def count_winning_choices(N, X, Y, bags):
    MOD = 998244353
    total_winning_choices = 0

    for mask in range(1 << N):
        takahashi_coins = 0
        aoki_coins = 0
        takahashi_silver = 0
        aoki_silver = 0
        
        for i in range(N):
            if mask & (1 << i):
                takahashi_coins += bags[i][0]
                takahashi_silver += bags[i][1]
            else:
                aoki_coins += bags[i][0]
                aoki_silver += bags[i][1]

        # Check if Takahashi can win with the current selection
        if (takahashi_coins > 0 or takahashi_silver > 0) and (aoki_coins > 0 or aoki_silver > 0):
            # Simulate the game
            while True:
                if takahashi_coins > 0:
                    takahashi_coins -= 1
                    takahashi_silver += X
                elif takahashi_silver > 0:
                    takahashi_silver -= 1
                else:
                    break

                if aoki_coins > 0:
                    aoki_coins -= 1
                    aoki_silver += Y
                elif aoki_silver > 0:
                    aoki_silver -= 1
                else:
                    break

            if takahashi_coins > 0 or takahashi_silver > 0:
                total_winning_choices += 1

    return total_winning_choices % MOD

# Read input
N, X, Y = map(int, input().split())
bags = [tuple(map(int, input().split())) for _ in range(N)]

# Get the result
result = count_winning_choices(N, X, Y, bags)

# Print the result
print(result)