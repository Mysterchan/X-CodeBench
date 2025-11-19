n = int(input())
a = list(map(int, input().split()))

# dp[i][0]: max sum after processing i-th element, with empty stack
# dp[i][1]: max sum after processing i-th element, with non-empty stack
# We only need to keep track of dp for previous step to optimize space

dp_empty = float('-inf')
dp_nonempty = float('-inf')

# At i=0 (before processing any element), stack is empty, sum=0
dp_empty = 0

for x in a:
    # If stack is empty before processing x, we must append x
    # So new dp_nonempty = dp_empty + x
    new_dp_nonempty = max(dp_nonempty + x, dp_empty + x)
    # If stack is non-empty before processing x, we can either append or pop
    # Append: dp_nonempty + x
    # Pop: dp_nonempty (pop last element, sum decreases by last element, but we don't track elements, so we must consider that pop removes last appended element)
    # But since we don't track elements, we must think carefully:
    # Actually, we can pop only if stack is non-empty, which means sum decreases by last appended element.
    # But we don't know last appended element here.
    # So we need a better approach.

# The above approach is incorrect because we don't know the last element to pop.

# Let's rethink the problem:

# The problem is equivalent to choosing a subsequence of the array with the constraint that
# at each step, we can either append the current element or pop the last appended element.
# The pop operation removes the last appended element, so the stack behaves like a stack of chosen elements.

# The key insight:
# The operations form a sequence of pushes and pops on a stack.
# The number of pops cannot exceed the number of pushes at any point.
# After processing all elements, the stack contains some subsequence of the original array,
# but the subsequence must be formed by a sequence of push/pop operations.

# The problem reduces to finding the maximum sum of a subsequence that can be formed by a sequence of push/pop operations,
# where at each step, you can push the current element or pop the last pushed element (if any).

# Another way to see it:
# The stack can be empty or non-empty.
# At each step:
# - If stack is empty, must push current element.
# - If stack is non-empty, can push or pop.

# Let's define dp[i][j] where j=0 or 1:
# dp[i][0]: max sum after processing i-th element with empty stack
# dp[i][1]: max sum after processing i-th element with non-empty stack

# Transitions:
# From dp[i-1][0]:
# - Must push a[i], so dp[i][1] = dp[i-1][0] + a[i]
# From dp[i-1][1]:
# - Push a[i]: dp[i][1] = max(dp[i][1], dp[i-1][1] + a[i])
# - Pop last element: dp[i][0] = max(dp[i][0], dp[i-1][1] - last_element)
# But we don't know last_element in dp.

# The problem is we don't know the last element to subtract when popping.

# Wait, the original code uses a stack to keep track of indices and sums.

# Let's try to simulate the stack with a single variable that keeps track of the sum and the stack size.

# But we need to know the last element to pop.

# So we can keep track of the sum and the stack as a list.

# But that would be O(N^2) in worst case.

# Let's try a different approach:

# Since the operations are push or pop, and we must process elements in order,
# the final stack is a subsequence of the original array,
# but the subsequence must be formed by a sequence of push/pop operations.

# The problem is equivalent to finding the maximum sum of a subsequence where
# the subsequence can be formed by a sequence of push/pop operations.

# The key is that the subsequence must be a stack-like subsequence:
# For each element, you can either push it or pop the last pushed element.

# This is equivalent to finding the maximum sum of a subsequence where
# the subsequence is a stack permutation of the original sequence.

# But since we can pop any number of times, the problem reduces to:
# At each step, we can either:
# - push current element (add it to sum)
# - pop last element (remove last element from sum)
# - but cannot pop if stack is empty

# So the problem is to find the maximum sum achievable by a sequence of push/pop operations.

# Let's try a greedy approach:

# We can simulate the stack with a list.

stack = []
total = 0
max_sum = float('-inf')

for x in a:
    # At each step, we can push or pop
    # If stack is empty, must push
    if not stack:
        stack.append(x)
        total += x
    else:
        # Decide whether to push or pop
        # If pushing x increases total sum, push
        # Else, pop last element
        if total + x >= total - stack[-1]:
            # push
            stack.append(x)
            total += x
        else:
            # pop
            total -= stack.pop()
            # After pop, must push current element
            stack.append(x)
            total += x
    max_sum = max(max_sum, total)

print(max_sum)