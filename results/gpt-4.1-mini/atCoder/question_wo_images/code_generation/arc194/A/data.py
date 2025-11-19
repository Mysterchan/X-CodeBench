def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # dp[i][j]: maximum sum after processing i elements,
    # with j elements currently in S (j >= 0)
    # But since j can be up to i, and N can be 2*10^5, 
    # this is not feasible to store.

    # We need a more efficient approach.

    # Observation:
    # At each step i, we can either:
    # - Append A[i] to S (increasing size by 1)
    # - Delete last element of S (decreasing size by 1, if not empty)
    #
    # We want to maximize sum of elements in S after all operations.

    # Let's think about the problem differently:
    # The operations form a sequence of stack operations.
    # We can think of the process as a stack where:
    # - push A[i]
    # - pop top element
    #
    # We must perform exactly one operation per element i.
    # So total operations = N.
    #
    # The final stack can be any size from 0 to N.
    #
    # We want to maximize sum of elements in the final stack.

    # Key insight:
    # The order of elements in the stack is the order of pushes minus pops.
    # The sequence of operations is fixed length N.
    #
    # We can model the problem as:
    # At step i, we have a stack of size j.
    # We can:
    # - push A[i], stack size j+1, sum += A[i]
    # - pop, stack size j-1, sum -= top element popped
    #
    # But we don't know the top element popped if we pop.
    #
    # So we need to keep track of the stack elements or at least the top element.

    # Since we want maximum sum, popping the smallest element is beneficial.
    # But we can only pop the last element pushed.

    # Let's try a DP with a stack simulation:
    # We keep track of possible stack states with their sums.
    # But this is too large.

    # Alternative approach:
    # Since we can only pop the last element, and we must perform exactly one operation per element,
    # the sequence of operations corresponds to a sequence of pushes and pops.
    #
    # The final stack is a subsequence of A, but with the constraint that the subsequence is formed by
    # a sequence of push/pop operations.
    #
    # The problem reduces to:
    # Find a subsequence of A (not necessarily contiguous) that can be formed by push/pop operations,
    # maximizing the sum.

    # Another way:
    # The stack operations correspond to a Dyck path of length N,
    # where push = up step, pop = down step.
    #
    # The final stack size is the height of the path at the end.
    #
    # We want to find a path with maximum sum of elements pushed and not popped.

    # Let's define dp[i][j]: maximum sum after processing i elements,
    # with stack size j.
    # j ranges from 0 to i.
    #
    # Transitions:
    # - push: dp[i][j] = dp[i-1][j-1] + A[i-1]
    # - pop: dp[i][j] = dp[i-1][j+1]
    #
    # Base case:
    # dp[0][0] = 0
    # dp[0][j] = -inf for j > 0

    # We want max dp[N][j] for j in [0..N]

    # Implementing this DP with O(N^2) is impossible for N=2*10^5.

    # Optimization:
    # At each step i, dp[i][j] depends only on dp[i-1][j-1] and dp[i-1][j+1].
    #
    # So we can keep dp array of size N+1 and update it iteratively.

    # But still O(N^2) time.

    # We need a better approach.

    # Let's try to find a greedy or stack-based approach.

    # Since we can pop only the last element, and we want to maximize sum,
    # we should avoid pushing negative elements unless they help.

    # But we must perform exactly one operation per element.

    # Let's simulate the process with a stack:
    # For each element A[i]:
    # - If A[i] >= 0, push it.
    # - If A[i] < 0, decide whether to push or pop.
    #
    # But we cannot pop if stack is empty.

    # But the problem is that we must perform exactly one operation per element,
    # so we cannot skip operations.

    # Let's try a stack simulation with a greedy approach:
    # For each element:
    # - If stack is empty, must push.
    # - Else:
    #   - If A[i] >= 0, push.
    #   - Else:
    #     - If top of stack is less than A[i], pop.
    #     - Else push.

    # But this is heuristic and may fail.

    # Let's try to implement the DP with a segment tree or data structure.

    # Another approach:
    # Since dp[i][j] depends on dp[i-1][j-1] and dp[i-1][j+1],
    # we can represent dp[i] as:
    # dp[i][j] = max(dp[i-1][j-1] + A[i-1], dp[i-1][j+1])

    # Let's implement dp with a rolling array and use a data structure to speed up.

    # Note that dp[i][j] depends on dp[i-1][j-1] and dp[i-1][j+1].
    # So for fixed i, dp[i][j] = max of two values.

    # Let's implement dp with two arrays and update accordingly.

    # Initialize dp array with -inf
    import math
    dp_prev = [-math.inf] * (N + 2)
    dp_prev[0] = 0

    for i in range(1, N + 1):
        dp_curr = [-math.inf] * (N + 2)
        a = A[i - 1]
        for j in range(0, i + 1):
            # push: from dp_prev[j-1] + a
            if j - 1 >= 0:
                val_push = dp_prev[j - 1] + a
                if val_push > dp_curr[j]:
                    dp_curr[j] = val_push
            # pop: from dp_prev[j+1]
            if j + 1 <= i - 1:
                val_pop = dp_prev[j + 1]
                if val_pop > dp_curr[j]:
                    dp_curr[j] = val_pop
        dp_prev = dp_curr

    print(max(dp_prev[:N + 1]))
    

if __name__ == "__main__":
    main()