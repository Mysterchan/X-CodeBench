t = int(input())
results = []
for _ in range(t):
    n, m = map(int, input().split())
    # Maximum players with perfect records is (M * (N - 1)) which means
    # each of the (N - 1) teams can have M players with wins.
    max_perfect_players = m * (n - 1)
    results.append(max_perfect_players)

# join and print results in a single output to optimize I/O
print("\n".join(map(str, results)))