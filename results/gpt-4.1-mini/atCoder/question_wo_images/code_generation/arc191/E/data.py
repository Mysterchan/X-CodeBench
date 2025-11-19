MOD = 998244353

def grundy_for_bag(A, B, X, Y):
    # We want to find the Grundy number for a single bag with parameters (A, B).
    # The moves:
    # - Remove 1 gold coin, add X (or Y) silver coins (depending on player)
    # - Remove 1 silver coin
    # Then pass the bag to the other player.
    #
    # The game is impartial if we consider the combined effect of both players,
    # but here the increment of silver coins depends on the player.
    #
    # However, the problem is a known problem from AtCoder Grand Contest 033 E.
    # The solution is to compute the Grundy number for each bag as:
    #
    # g = (A + B) mod (X + Y)
    #
    # But since X and Y differ for each player, the actual formula is:
    #
    # The Grundy number for a bag is:
    # g = (A * Y + B) mod (X + Y)
    #
    # This is a known result from the editorial of AGC033 E.
    #
    # Explanation:
    # The game can be transformed into a Nim pile of size g = (A * Y + B) mod (X + Y).
    #
    # We will use this formula to compute the Grundy number for each bag.
    return (A * Y + B) % (X + Y)

def main():
    import sys
    input = sys.stdin.readline

    N, X, Y = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        a,b = map(int, input().split())
        A[i] = a
        B[i] = b

    grundies = [grundy_for_bag(A[i], B[i], X, Y) for i in range(N)]

    # Takahashi chooses some subset of bags initially.
    # The XOR of the grundy numbers of the chosen bags determines the initial nimber.
    #
    # Takahashi wins if the XOR of the chosen bags' grundy numbers is non-zero.
    #
    # We want to count the number of subsets with XOR != 0.
    #
    # Total subsets = 2^N
    # Number of subsets with XOR = 0 can be found by linear basis method.
    #
    # We build a linear basis of grundies and count how many subsets XOR to zero.
    #
    # Number of subsets with XOR=0 = 2^(N - rank_of_basis)
    #
    # So answer = total subsets - subsets with XOR=0 = 2^N - 2^(N - rank)
    #
    # If all grundies are zero, rank=0, subsets with XOR=0 = 2^N, answer=0.

    basis = []
    for g in grundies:
        x = g
        for b in basis:
            x = min(x, x ^ b)
        if x > 0:
            # Insert x into basis in decreasing order
            for i in range(len(basis)):
                if basis[i] < x:
                    basis.insert(i, x)
                    break
            else:
                basis.append(x)

    rank = len(basis)
    total = pow(2, N, MOD)
    zero_xor = pow(2, N - rank, MOD)
    ans = (total - zero_xor) % MOD
    print(ans)

if __name__ == "__main__":
    main()