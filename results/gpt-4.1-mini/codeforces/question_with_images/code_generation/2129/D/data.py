MOD = 998244353

def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        # s_i = score of cell i after all coloring
        # s_i = number of times cell i was the nearest black cell to newly colored cells (except itself)
        # Initially all cells white, score 0
        # At step i (1-based), color p_i black
        # For i>1, find nearest black cell to p_i, increase its score by 1
        # If multiple nearest, choose lowest index

        # We want to count permutations p that produce s (with some s_i possibly -1)

        # Key observations:
        # - The first colored cell p_1 has no score increment (no nearest black cell before)
        #   So s_{p_1} = 0 necessarily.
        # - For each other cell p_i (i>1), it increments the score of the nearest black cell to p_i.
        # - The score s_i is the count of how many times cell i was the nearest black cell to newly colored cells.

        # We want to count permutations p = [p_1,...,p_n] such that the final s matches given s (with -1 as unknown).

        # Approach:
        # The process can be seen as building a tree rooted at p_1:
        # Each newly colored cell p_i (i>1) connects to its nearest black cell (parent).
        # The score s_i is the number of children of node i in this tree.
        #
        # So s_i = number of children of node i in the tree.
        #
        # The tree has n nodes, with exactly n-1 edges.
        # sum of s_i = n-1 (since total edges = n-1)
        #
        # If s_i != -1, it fixes the number of children of node i.
        # If s_i == -1, the number of children is unknown.
        #
        # We want to count the number of rooted trees with given partial children counts s_i (some fixed, some unknown),
        # and count the number of permutations p that produce this tree.
        #
        # But the problem is more subtle because the "nearest black cell" depends on positions.
        #
        # However, the problem is known and can be solved by DP:
        #
        # The key is to consider the order of coloring as a BFS order of the tree rooted at p_1.
        #
        # The first colored cell p_1 is the root.
        # Then the children of p_1 are colored next, then their children, etc.
        #
        # The score s_i is the number of children of node i.
        #
        # So the problem reduces to counting the number of rooted trees with given children counts s_i,
        # where some s_i are fixed, some unknown.
        #
        # The number of permutations p that produce the tree is:
        # For each node, the order of coloring its children can be any permutation.
        # So total ways = product over nodes of (children_count_i)! times ways to arrange subtrees.
        #
        # We can solve by DP on the tree structure.
        #
        # But we don't know the tree structure, only children counts.
        #
        # So we need to count the number of trees with given children counts s_i (some fixed, some unknown).
        #
        # The problem reduces to counting the number of rooted trees with given children counts s_i,
        # where sum of s_i = n-1.
        #
        # If s_i != -1, children count fixed.
        # If s_i == -1, children count unknown (can be 0..n-1).
        #
        # We want to count the number of integer sequences s_i' that match s_i where s_i != -1,
        # and sum s_i' = n-1.
        #
        # For each such sequence, the number of trees with that children count sequence is:
        # number of ways to arrange children subtrees * product of factorial(children_count_i)
        #
        # But the tree structure is uniquely determined by children counts and order of children.
        #
        # Actually, the number of trees with given children counts is:
        # number of ways to assign children to nodes = multinomial coefficient:
        # (n-1)! / product of factorial(children_count_i)
        #
        # Because the tree is rooted and ordered by children order.
        #
        # But the problem states that the order of coloring is the order of BFS traversal of the tree,
        # so the order of children matters.
        #
        # So total number of permutations p that produce the tree with children counts s_i is:
        # (n-1)! / product of factorial(children_count_i)
        #
        # So the problem reduces to:
        # - Find all sequences s' matching s (fixed s_i or any if s_i == -1), sum s' = n-1
        # - For each s', compute ways = (n-1)! / product factorial(s'_i)
        # - Sum over all s'
        #
        # This is a classic stars and bars problem with some fixed values.
        #
        # Implementation:
        # - Let fixed_sum = sum of fixed s_i
        # - Let unknown_count = number of s_i == -1
        # - We need to distribute (n-1 - fixed_sum) children among unknown_count nodes
        # - Each unknown s_i >= 0
        #
        # For each distribution, compute ways = (n-1)! / product factorial(s_i)
        #
        # Since n <= 100, unknown_count <= n, and sum <= n-1, we can do DP to count sum of multinomial coefficients.
        #
        # We'll do DP over unknown nodes:
        # dp[i][j] = sum of ways for first i unknown nodes with total children j
        #
        # For each unknown node, try all possible children count k from 0 to (n-1 - fixed_sum)
        #
        # To handle division by factorial, we use precomputed factorials and inverse factorials.
        #
        # We'll compute:
        # ways = (n-1)! * sum over all distributions of 1 / product factorial(s_i)
        #
        # So dp will store sum of 1 / product factorial(s_i) for partial assignments.
        #
        # Finally multiply dp[unknown_count][n-1 - fixed_sum] by (n-1)! modulo MOD.
        #
        # If fixed_sum > n-1, answer = 0
        # If any fixed s_i < 0 or > n-1, answer = 0
        #
        # Also, s_{p_1} = 0, so the root must have score 0.
        # We don't know p_1, but s_i = 0 for root.
        # So among s_i, at least one must be 0 (the root).
        #
        # If no s_i == 0 fixed, then root can be any node with s_i == -1 or s_i == 0.
        #
        # So we must consider all possible roots:
        # For each i in [1..n]:
        #   if s_i == 0 or s_i == -1 (can be 0)
        #   set s_i = 0 (if -1)
        #   check if sum of fixed s_i <= n-1
        #   count ways for remaining unknowns
        #   sum over all possible roots
        #
        # But if s_i fixed != 0, cannot be root.
        #
        # So we try all possible roots i:
        #   if s_i == -1 or s_i == 0:
        #       fix s_i = 0
        #       fix other s_j as given
        #       count ways
        #
        # Sum over all roots.
        #
        # If no root candidate, answer = 0

        # Precompute factorials and inverse factorials
        max_n = 100
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(2, max_n + 1):
            fact[i] = fact[i-1] * i % MOD

        def modinv(x):
            return pow(x, MOD-2, MOD)

        inv_fact[max_n] = modinv(fact[max_n])
        for i in range(max_n-1, 0, -1):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

        def comb(n, k):
            if k > n or k < 0:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n-k] % MOD

        # DP to sum over distributions of children counts for unknown nodes
        # dp[i][j] = sum of 1 / product factorial(children counts) for first i unknown nodes with total j children
        # We'll store dp as integers modulo MOD, using inverse factorials

        def count_ways(fixed, unknown_count, total):
            # fixed: dict {index: fixed children count}
            # unknown_count: number of unknown nodes
            # total: total children to distribute among unknown nodes

            # We only need to consider unknown nodes, their indices are not important here
            # We'll do DP over unknown_count nodes

            dp = [0] * (total + 1)
            dp[0] = 1

            for _ in range(unknown_count):
                ndp = [0] * (total + 1)
                for j in range(total + 1):
                    if dp[j] == 0:
                        continue
                    # try k children for this unknown node
                    for k in range(total - j + 1):
                        # add dp[j] * inv_fact[k]
                        val = dp[j] * inv_fact[k] % MOD
                        ndp[j + k] = (ndp[j + k] + val) % MOD
                dp = ndp
            return dp[total]

        # Main logic:
        # Try each possible root i:
        #   if s_i == -1 or s_i == 0:
        #       fix s_i = 0
        #       check other fixed s_j
        #       sum fixed s_j
        #       unknown_count = number of s_j == -1 except root
        #       total = n-1 - fixed_sum
        #       if total < 0: continue
        #       ways = (n-1)! * count_ways(...) mod MOD
        # sum over all roots

        ans = 0
        for root in range(n):
            if s[root] != -1 and s[root] != 0:
                continue
            # Build fixed dict
            fixed = {}
            fixed_sum = 0
            unknown_count = 0
            for i in range(n):
                if i == root:
                    fixed[i] = 0
                    fixed_sum += 0
                else:
                    if s[i] == -1:
                        unknown_count += 1
                    else:
                        if s[i] < 0 or s[i] > n-1:
                            break
                        fixed[i] = s[i]
                        fixed_sum += s[i]
            else:
                # no break
                if fixed_sum > n - 1:
                    continue
                total = n - 1 - fixed_sum
                ways_inv = count_ways(fixed, unknown_count, total)
                ways = fact[n - 1] * ways_inv % MOD
                ans = (ans + ways) % MOD

        print(ans)

if __name__ == "__main__":
    solve()