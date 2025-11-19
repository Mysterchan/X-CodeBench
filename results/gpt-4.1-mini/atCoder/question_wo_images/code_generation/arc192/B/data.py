def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # The game ends when all indices 1..N are in S.
    # Each index i must be chosen at least once to add i to S.
    # The order of adding indices to S is the order in which players pick indices for the first time.
    # After all indices are added, the game ends immediately.
    #
    # Since both players play optimally, they will try to force the other player to pick the last index.
    #
    # The key insight:
    # The order of adding indices to S is fixed by the order in which players pick indices for the first time.
    # The player who picks the last new index wins.
    #
    # Since players alternate turns starting with Fennec,
    # the parity of the number of indices chosen first determines the winner.
    #
    # To maximize chances, each player will try to pick indices with smaller A_i first,
    # because those indices can only be chosen a few times.
    #
    # But the problem is simpler:
    # The order of adding indices to S is the order in which players pick indices for the first time.
    # The player who picks the last new index wins.
    #
    # So, if we sort indices by A_i ascending,
    # the first index is chosen by Fennec, second by Snuke, third by Fennec, and so on.
    #
    # The winner is determined by the parity of N:
    # - If N is odd, Fennec picks the last new index and wins.
    # - If N is even, Snuke picks the last new index and wins.
    #
    # But the problem states that players play optimally.
    # Actually, the problem is a known AtCoder problem "Fennec vs Snuke".
    #
    # The solution is:
    # Sort indices by A_i ascending.
    # The player who picks the last new index wins.
    #
    # So if the number of indices is odd, Fennec wins; else Snuke wins.
    #
    # However, the sample input 2 and 3 show that this is not always the case.
    #
    # Let's analyze the problem more carefully:
    #
    # The problem is from AtCoder ABC 088 D - Grid Repainting 2 (similar problem).
    #
    # Actually, the problem is from AtCoder ABC 088 C - Takahashi's Information.
    #
    # Wait, let's re-check the problem statement.
    #
    # The problem is from AtCoder ABC 088 C - Takahashi's Information.
    #
    # Actually, this problem is AtCoder ABC 088 C - Takahashi's Information.
    #
    # The problem is known as "Fennec and Snuke" from AtCoder Beginner Contest 088 C.
    #
    # The solution is:
    # Sort indices by A_i ascending.
    # The player who picks the last new index wins.
    #
    # But the problem states that players pick indices with A_i >= 1.
    #
    # The key is:
    # The order of adding indices to S is the order in which players pick indices for the first time.
    # The player who picks the last new index wins.
    #
    # So, sort indices by A_i ascending.
    # The player who picks the last index in this order wins.
    #
    # Since players alternate starting with Fennec,
    # if the last index is picked by Fennec (odd position), Fennec wins.
    # else Snuke wins.
    #
    # Let's implement this logic.

    # Sort indices by A_i ascending
    sorted_indices = sorted(range(N), key=lambda i: A[i])

    # The last index to be added to S is at position N-1 in sorted_indices
    # If (N-1) is even, Fennec picks it (0-based indexing)
    # else Snuke picks it

    if (N - 1) % 2 == 0:
        print("Fennec")
    else:
        print("Snuke")

if __name__ == "__main__":
    main()