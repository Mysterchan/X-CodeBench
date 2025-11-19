def count_winning_combinations(N, X, Y, bags):
    MOD = 998244353
    winning_count = 0

    for mask in range(1 << N):
        takahashi_bags = []
        aoki_bags = []
        
        for i in range(N):
            if mask & (1 << i):
                takahashi_bags.append(bags[i])
            else:
                aoki_bags.append(bags[i])
        
        if can_takahashi_win(takahashi_bags, aoki_bags, X, Y):
            winning_count += 1
            winning_count %= MOD

    return winning_count

def can_takahashi_win(takahashi_bags, aoki_bags, X, Y):
    takahashi_coins = sum(a[0] for a in takahashi_bags)
    takahashi_silver = sum(a[1] for a in takahashi_bags)
    aoki_coins = sum(a[0] for a in aoki_bags)
    aoki_silver = sum(a[1] for a in aoki_bags)

    # If Aoki has no coins and Takahashi has coins, Takahashi wins
    if aoki_coins == 0 and takahashi_coins > 0:
        return True

    # If both have no coins, Takahashi cannot win
    if takahashi_coins == 0 and aoki_coins == 0:
        return False

    # If Takahashi has no coins, he loses
    if takahashi_coins == 0:
        return False

    # Game simulation logic
    while True:
        if takahashi_coins > 0:
            # Takahashi can play
            if takahashi_coins > 0:
                takahashi_coins -= 1
                takahashi_silver += X
            else:
                break
        else:
            break

        if aoki_coins > 0:
            # Aoki can play
            if aoki_coins > 0:
                aoki_coins -= 1
                aoki_silver += Y
            else:
                break
        else:
            break

    return takahashi_coins > 0

import sys
input = sys.stdin.read
data = input().splitlines()

N, X, Y = map(int, data[0].split())
bags = [tuple(map(int, line.split())) for line in data[1:N+1]]

result = count_winning_combinations(N, X, Y, bags)
print(result)