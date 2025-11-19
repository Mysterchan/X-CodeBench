t = int(input())
for _ in range(t):
    n = int(input())
    # In a double-elimination tournament with n teams,
    # total matches played = 2*n - 2
    # Explanation:
    # Each team except the final winner loses exactly twice (except the winner who loses once or zero times).
    # Since each match eliminates one loss, total matches = total losses = 2*(n-1).
    print(2 * n - 2)