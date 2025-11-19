import sys
input = sys.stdin.readline
MOD = 998244353

# Precompute factorials and inverse factorials for n up to 100
MAXN = 100
fact = [1] * (MAXN + 1)
inv_fact = [1] * (MAXN + 1)
for i in range(2, MAXN + 1):
    fact[i] = fact[i-1] * i % MOD

def modinv(x):
    return pow(x, MOD-2, MOD)

inv_fact[MAXN] = modinv(fact[MAXN])
for i in range(MAXN-1, 0, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        # Count how many cells have score 0, how many have fixed positive scores, and how many unknown
        # The problem can be solved by DP on the number of cells with score 0 and positive scores
        # The key insight:
        # - The cell colored at step 1 has score 0
        # - Each subsequent step colors a cell and increments score of the nearest black cell
        # - The sum of all scores is n-1 (since each step except the first increments one score)
        # - The score array s corresponds to the number of times each cell was the nearest black cell when coloring others

        # We want to count permutations p that produce s (with some unknowns)
        # The problem reduces to counting ways to assign the order of coloring cells so that the score constraints hold

        # Let's analyze the problem:
        # The cell colored at step 1 has score 0
        # For each cell with score > 0, it must have been the nearest black cell for that many times
        # The sum of scores is n-1

        # We can think of the coloring order as a rooted tree with n nodes:
        # - The root is the cell colored first (score 0)
        # - Each other cell points to the nearest black cell that increased its score
        # - The score of a cell is the number of children in this tree

        # So the score array s corresponds to the outdegree of each node in the tree
        # The problem reduces to counting the number of permutations p that produce a tree with outdegree = s_i

        # Since the tree is rooted and the order of coloring corresponds to a BFS or DFS order consistent with the tree,
        # the number of permutations is the number of ways to order the nodes so that the parent is colored before children.

        # The number of such permutations is:
        # n! / (product of factorials of subtree sizes)
        # But since we only have outdegrees, we can use a known formula:
        # The number of permutations consistent with a rooted tree with outdegrees s_i is:
        #   (n-1)! / (product of factorials of s_i)
        # Because the root is fixed (colored first), and the children can be permuted in any order.

        # However, we have unknown scores (-1), so we must count all possible assignments of scores consistent with the constraints.

        # Constraints:
        # - sum of scores = n-1
        # - scores[i] >= 0
        # - fixed scores must be matched
        # - unknown scores can be any >= 0

        # So the problem reduces to counting the number of integer solutions to:
        # sum of unknown scores = n-1 - sum of fixed scores
        # with unknown scores >= 0

        # For each such solution, the number of permutations is:
        # (n-1)! / product of factorials of all scores

        # We sum over all possible assignments of unknown scores.

        # Implementation plan:
        # 1. Identify fixed scores and unknown scores
        # 2. Calculate sum_fixed = sum of fixed scores (ignoring -1)
        # 3. Let k = number of unknown scores
        # 4. We want to find sum over all vectors x of length k with sum x = n-1 - sum_fixed:
        #    sum ( (n-1)! / (product of factorials of fixed scores and x) )
        # 5. Use DP to compute sum of 1/(product of factorials of x_i) over all x with sum x = S
        # 6. Multiply by (n-1)! / product of factorials of fixed scores

        # Edge cases:
        # - If sum_fixed > n-1 => no solution
        # - If any fixed score < 0 or > n-1 => no solution
        # - If s[i] != -1 and s[i] > n-1 => no solution

        # Precompute factorial inverses for factorial division

        fixed_scores = []
        unknown_count = 0
        sum_fixed = 0
        for val in s:
            if val == -1:
                unknown_count += 1
            else:
                if val < 0 or val > n-1:
                    # invalid score
                    print(0)
                    break
                sum_fixed += val
        else:
            if sum_fixed > n-1:
                print(0)
                continue

            S = n - 1 - sum_fixed
            if S < 0:
                print(0)
                continue

            # Precompute product of factorials of fixed scores
            prod_fixed_fact = 1
            for val in s:
                if val != -1:
                    prod_fixed_fact = (prod_fixed_fact * fact[val]) % MOD

            # DP to compute sum of 1/(product of factorials of unknown scores) for all unknown scores summing to S
            # dp[i][j] = sum of 1/(product factorials) for first i unknowns summing to j
            # Since unknown_count <= n <= 100 and S <= n-1 <= 99, this is feasible

            if unknown_count == 0:
                # no unknowns, check if sum_fixed == n-1
                if sum_fixed == n-1:
                    # number of permutations = (n-1)! / product of factorials of scores
                    ans = fact[n-1] * modinv(prod_fixed_fact) % MOD
                    print(ans)
                else:
                    print(0)
                continue

            dp = [0] * (S + 1)
            dp[0] = 1  # base case: zero unknowns sum to 0 with product=1

            for _ in range(unknown_count):
                ndp = [0] * (S + 1)
                for curr_sum in range(S + 1):
                    if dp[curr_sum] == 0:
                        continue
                    # try all possible values for this unknown score from 0 to S - curr_sum
                    # To optimize, precompute inverse factorials and use prefix sums

                    # We'll do a prefix sum over factorial inverses to speed up
                    # But since S is small, a nested loop is acceptable

                    for val in range(S - curr_sum + 1):
                        # add dp[curr_sum] * inv_fact[val]
                        ndp[curr_sum + val] = (ndp[curr_sum + val] + dp[curr_sum] * inv_fact[val]) % MOD
                dp = ndp

            # dp[S] now contains sum of 1/(product factorials of unknown scores) for sum unknown scores = S

            ans = fact[n-1] * modinv(prod_fixed_fact) % MOD
            ans = ans * dp[S] % MOD
            print(ans)

if __name__ == "__main__":
    main()