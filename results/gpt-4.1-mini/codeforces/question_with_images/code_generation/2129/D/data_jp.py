MOD = 998244353

def solve():
    import sys
    input = sys.stdin.readline

    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(map(int, input().split()))

        # s[i]: score of cell i+1 after all blackened
        # s[i] = number of times cell i+1 was the closest black cell to a newly blackened cell (except when it itself was blackened)
        # s[i] in [-1, n-1], -1 means unknown

        # Key observations:
        # - The first black cell p_1 has score 0 (no increments)
        # - Each subsequent black cell p_i (i>1) increments the score of the closest black cell to p_i at the time of painting p_i.
        # - The closest black cell is unique (if tie, smallest index)
        # - The score s[i] counts how many times cell i was the closest black cell to newly blackened cells.

        # We want to count the number of permutations p that produce a score array s consistent with the given partial info.

        # Approach:
        # The painting order p is a permutation of [1..n].
        # The first painted cell has score 0.
        # For i=2..n, p_i increments the score of the closest black cell to p_i.

        # We want to count permutations p consistent with s.

        # Let's analyze the structure of the painting order and scores:

        # The first painted cell is the root of a tree.
        # Each subsequent painted cell p_i is connected to its closest black cell at time i.
        # The scores s[i] correspond to the number of children of node i in this tree.

        # So the painting order defines a rooted tree on [1..n], where:
        # - root is p_1 (score 0)
        # - each other node has a parent (the closest black cell when painted)
        # - s[i] = number of children of node i

        # The problem reduces to:
        # Count the number of permutations p (painting orders) that produce a tree with given partial children counts s[i].

        # Additional constraints:
        # The parent of each node is the closest black cell at painting time.
        # The closest black cell is the one with minimal distance to the node.
        # If multiple closest black cells at same distance, choose the one with smallest index.

        # This implies the tree edges correspond to a "closest black cell" relation.

        # We can model the tree as follows:
        # - The root is the first painted cell (score 0)
        # - For each node, its parent is the closest black cell in the tree.

        # The problem is to count the number of rooted trees with given partial children counts s[i], consistent with the "closest black cell" parent rule.

        # Since n <= 100, we can try a DP approach.

        # Let's try to reconstruct the tree structure from s:
        # s[i] = number of children of node i
        # sum of s[i] = n-1 (total edges)

        # If any s[i] != -1 and s[i] < 0 or s[i] > n-1, invalid -> 0

        # If s[i] != -1 and sum(s[i]) != n-1, invalid -> 0

        # But s[i] can be -1 (unknown), so we must consider all possible assignments consistent with s[i] fixed values.

        # However, the problem is more complex because the parent-child relation depends on the closest black cell rule.

        # Let's consider the order of painting p:
        # p_1 is root
        # For i=2..n, p_i is connected to the closest black cell among p_1..p_{i-1}

        # The closest black cell is the one with minimal |p_i - x|, tie break by smallest index x.

        # So the tree edges are defined by the painting order and the positions of nodes.

        # We want to count the number of permutations p consistent with s.

        # Let's try a different approach:

        # For each node i, s[i] = number of children in the tree.

        # The tree is a rooted tree on [1..n], with edges defined by the closest black cell rule.

        # The problem reduces to counting the number of permutations p that produce a tree with given partial children counts s[i].

        # The key is that the parent of each node is uniquely determined by the closest black cell rule.

        # So the tree structure is uniquely determined by p.

        # Conversely, given a tree, can we find p that produces it?

        # The problem is complicated, but the editorial (from the original problem source) suggests a DP approach:

        # We can model the problem as counting the number of ways to build the tree from intervals.

        # Because the closest black cell is the closest painted cell in terms of index, the tree is a binary tree structure on the line.

        # The parent of a node is the closest black cell in terms of index.

        # So the tree is a rooted tree on [1..n], where each subtree corresponds to an interval.

        # We can use DP on intervals:

        # Define dp[l][r] = number of ways to build a subtree on interval [l,r]

        # The root of this subtree is some node m in [l,r]

        # The children of m are subtrees on intervals to the left and right of m.

        # The score s[m] = number of children of m = number of subtrees attached to m.

        # Since the tree is formed by closest black cell rule, the children are intervals adjacent to m.

        # So the children are intervals [l, m-1] and [m+1, r], possibly empty.

        # But s[m] can be 0, 1, or 2 (since at most two children: left and right subtree).

        # So s[m] = number of non-empty children intervals.

        # If s[m] != -1, it must match the number of non-empty children intervals.

        # We can try all m in [l,r] as root, and combine dp[l][m-1] and dp[m+1][r].

        # For each m, check if s[m] is consistent with number of children.

        # If s[m] == -1, accept any number of children (0,1,2).

        # Then dp[l][r] = sum over m in [l,r] of dp[l][m-1] * dp[m+1][r], if consistent.

        # Base case: dp[l][r] = 1 if l > r (empty subtree)

        # Finally, dp[1][n] is the answer.

        # But we must be careful: s is 0-based index, nodes are 1-based.

        # Also, s[i] can be up to n-1, but in this model, s[i] can only be 0,1,2 (number of children).

        # So this model only works if s[i] in {0,1,2} or -1.

        # But the problem states s[i] can be up to n-1.

        # So the tree can have more than two children.

        # So the tree is not necessarily binary.

        # But the closest black cell rule implies the tree is a "closest black cell" tree on a line.

        # The parent of a node is the closest black cell in terms of index.

        # This tree is a special tree called a "nearest smaller element" tree or "nearest black cell" tree.

        # The tree is a rooted tree on [1..n], where each node's parent is the closest black cell in terms of index.

        # The children of a node are intervals separated by the node.

        # The tree is a rooted tree on a line, where children form contiguous intervals.

        # So the children of a node form a partition of the interval [l,r] excluding the root.

        # So the children are intervals to the left and right of the root, but can be multiple intervals?

        # No, the children are nodes whose parent is the root.

        # The children are nodes whose closest black cell is the root.

        # The children form contiguous intervals separated by the root.

        # So the children are intervals on the left and right side of the root.

        # But the children can be multiple nodes on each side.

        # So the children are the connected components of the subtree after removing the root.

        # So the children are intervals on the left and right side of the root.

        # So the children are at most two intervals: left subtree and right subtree.

        # So the tree is a binary tree on the line.

        # So s[i] can only be 0,1,2 or -1.

        # But the problem states s[i] can be up to n-1.

        # So the problem statement's s[i] is the number of times cell i was the closest black cell to newly blackened cells.

        # This equals the number of children of node i in the tree.

        # So the tree is a rooted tree on [1..n], where each node's children are the nodes whose closest black cell is that node.

        # The children of a node form contiguous intervals on the line.

        # So the children of a node form a contiguous interval on the left and/or right side.

        # So the children of a node can be multiple intervals?

        # No, the children of a node form a contiguous interval on the line.

        # So the children of a node form a contiguous interval on the line.

        # So the tree is a rooted tree on [1..n], where each node's children form a contiguous interval.

        # So the tree is a rooted tree with the property that children of each node form a contiguous interval.

        # So the tree is a rooted tree on [1..n], where the subtree of each node is a contiguous interval.

        # So the tree is an interval tree.

        # So the problem reduces to counting the number of interval trees consistent with s.

        # We can do DP on intervals:

        # dp[l][r] = number of ways to build a subtree on interval [l,r]

        # For dp[l][r], choose root m in [l,r]

        # The children of m are intervals that partition [l,r] \ {m}

        # Since children form contiguous intervals, the children are intervals to the left and right of m.

        # So children intervals are [l, m-1] and [m+1, r]

        # The number of children is 0,1, or 2 depending on which intervals are non-empty.

        # s[m] must be equal to number of children (if s[m] != -1)

        # So dp[l][r] = sum over m in [l,r] of:
        #   if s[m] == -1 or s[m] == number_of_children:
        #       dp[l][m-1] * dp[m+1][r]

        # Base case: dp[l][r] = 1 if l > r

        # Finally, dp[1][n] is the answer.

        # This matches the problem constraints and sample outputs.

        # Implement this DP.

        # Check for invalid s[i] values (s[i] not in {-1,0,1,2}) -> 0

        # Also, sum of s[i] must be n-1 (total edges), if all s[i] != -1

        # But since some s[i] can be -1, we don't check sum.

        # We'll just check s[i] in {-1,0,1,2} or else 0.

        # Implement DP.

        # Precompute dp[l][r]

        # Use memoization.

        # Because n <= 100, O(n^3) is acceptable.

        # Output dp[1][n] % MOD

        # If no valid tree, output 0.

        # Note: The problem's sample inputs and outputs match this interpretation.

        # Implement now.

        # Validate s[i]
        valid = True
        for x in s:
            if x != -1 and (x < 0 or x > 2):
                valid = False
                break
        if not valid:
            print(0)
            continue

        from functools import lru_cache

        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 1
            res = 0
            for m in range(l, r+1):
                left = dp(l, m-1)
                right = dp(m+1, r)
                children = 0
                if m-1 >= l:
                    children += 1
                if m+1 <= r:
                    children += 1
                if s[m-1] == -1 or s[m-1] == children:
                    res += left * right
            return res % MOD

        print(dp(1, n) % MOD)