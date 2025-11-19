import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = int(input())

# MEX table for pairs (x,y) with x,y in {0,1,2}
# MEX(x,y) = smallest non-negative integer not in {x,y}
# Possible pairs and their MEX:
# (0,0)->1, (0,1)->2, (0,2)->1
# (1,0)->2, (1,1)->0, (1,2)->0
# (2,0)->1, (2,1)->0, (2,2)->0
mex = [
    [1, 2, 1],
    [2, 0, 0],
    [1, 0, 0]
]

# We want to assign to each position i a value B_i in {0,1,2}
# with counts A0, A1, A2 respectively, to maximize sum of MEX(B_i, B_{P_i})

# Note that the graph defined by edges (i, P_i) is a permutation, so it consists of cycles.
# The sum is over all i of MEX(B_i, B_{P_i}).
# Since P is a permutation, edges form cycles.
# For each cycle C = (c_0, c_1, ..., c_{k-1}), the contribution is:
# sum_{j=0 to k-1} MEX(B_{c_j}, B_{c_{(j+1) mod k}})

# We want to assign values to nodes in each cycle to maximize sum of MEX on edges,
# subject to global counts A0, A1, A2.

# Key observations:
# - The problem reduces to assigning values to cycles to maximize sum of MEX on edges.
# - The total counts of 0,1,2 assigned over all cycles must be A0,A1,A2.
# - We want to precompute for each cycle the maximum possible sum for each possible count triple (a0,a1,a2) with a0+a1+a2=cycle_length.
#   But cycle length can be up to N, so this is impossible directly.

# Alternative approach:
# Since MEX values are small and fixed, and only 3 values, we can consider the edges' MEX values for pairs of assigned values.

# Let's analyze the MEX matrix:

# mex matrix:
#    0 1 2
# 0 [1 2 1]
# 1 [2 0 0]
# 2 [1 0 0]

# The maximum MEX value is 2, achieved only by pairs (0,1) or (1,0).

# So edges between 0 and 1 nodes give 2 points.
# Edges between 0 and 0 or 0 and 2 or 2 and 0 give 1 point.
# Edges between 1 and 1 or 1 and 2 or 2 and 1 or 2 and 2 give 0 points.

# So to maximize sum, we want as many edges between 0 and 1 as possible.

# Let's consider the problem per cycle:

# For a cycle of length k, the edges form a cycle of length k.

# We want to assign values in {0,1,2} to nodes in the cycle to maximize sum of MEX on edges.

# Since edges are between consecutive nodes in the cycle, the sum is sum over edges of mex(B_i, B_{i+1}).

# We want to maximize sum of mex over edges in the cycle.

# Since 2 is the max mex, edges between 0 and 1 give 2 points.

# Edges between 0 and 0 or 0 and 2 or 2 and 0 give 1 point.

# Edges between 1 and 1 or 1 and 2 or 2 and 1 or 2 and 2 give 0 points.

# So to maximize sum, we want to maximize number of edges between 0 and 1.

# Also, 2's are "bad" because edges involving 2 and 1 or 2 and 2 give 0 points.

# Edges involving 2 and 0 give 1 point.

# So 2's are less valuable than 0 and 1.

# Let's consider the cycle as a ring, and assign values to nodes to maximize sum of mex on edges.

# Let's consider only 0 and 1 assignments first.

# For a cycle of length k, if we assign values alternating 0 and 1, the edges are all between 0 and 1, so each edge gives 2 points.

# Since the cycle length is k, number of edges is k.

# So total sum is 2*k.

# But we must have counts A0 and A1 matching the total counts over all cycles.

# So for each cycle, if length is even, we can assign alternating 0 and 1 perfectly.

# For odd length cycles, alternating 0 and 1 will have one edge between same values (0-0 or 1-1), which gives 1 or 0 points.

# Let's check for odd length cycles:

# For odd length cycle, alternating 0 and 1 assignment will have k edges, but one edge will be between same values.

# For example, cycle length 3:

# Assign 0,1,0:

# Edges: (0,1)=2, (1,0)=2, (0,0)=1

# Sum = 2+2+1=5

# Assign 1,0,1:

# Edges: (1,0)=2, (0,1)=2, (1,1)=0

# Sum=2+2+0=4

# So better to start with 0.

# So for odd length cycles, alternating 0 and 1 starting with 0 gives sum = 2*(k-1) + 1 = 2k -1

# For even length cycles, alternating 0 and 1 gives sum = 2*k

# Now, what if we assign some 2's?

# Since edges involving 2 and 1 or 2 and 2 give 0 points, and edges involving 2 and 0 give 1 point.

# So 2's reduce the total sum compared to 0 and 1 assignments.

# So to maximize sum, we want to assign only 0 and 1 values to nodes.

# But the problem requires that the total counts of 0,1,2 over all nodes equal A0,A1,A2.

# So if A2 > 0, we must assign some nodes to 2.

# So we want to assign 2's to nodes where it reduces the total sum the least.

# Since edges involving 2 and 0 give 1 point, edges involving 2 and 1 or 2 and 2 give 0 points.

# So 2's adjacent to 0's give 1 point, adjacent to 1's give 0 points.

# So to minimize loss, assign 2's in a way that edges involving 2 and 0 are maximized.

# But this is complicated.

# Alternative approach:

# Since the problem is large, we need an O(N) solution.

# Let's consider the following:

# The graph is a permutation, so it consists of cycles.

# For each cycle, we can assign values to nodes to maximize sum of mex on edges in that cycle.

# The total sum is sum over cycles.

# So we can process each cycle independently.

# For each cycle, we want to find the maximum sum achievable for all possible assignments of counts of 0,1,2 in that cycle.

# But this is too large.

# Let's consider only 0 and 1 assignments first.

# For a cycle of length k:

# - If we assign only 0 and 1 alternating, sum is:

#   - 2*k if k even

#   - 2*k - 1 if k odd

# - The counts of 0 and 1 in the cycle are:

#   - For even k: k/2 zeros and k/2 ones

#   - For odd k: (k+1)/2 zeros and (k-1)/2 ones (if start with 0)

# So for each cycle, the counts of 0 and 1 are fixed if we assign alternating 0 and 1 starting with 0.

# Now, if we want to assign 2's, the sum decreases.

# So the best sum for a cycle is achieved by assigning only 0 and 1 alternating starting with 0.

# So the problem reduces to:

# We have cycles with lengths k_1, k_2, ..., k_m.

# For each cycle, the best assignment is alternating 0 and 1 starting with 0, with counts:

#   zeros = (k+1)//2

#   ones = k//2

# sum = 2*k if k even else 2*k - 1

# Now, the total counts of zeros and ones assigned in all cycles are:

# sum_zeros = sum over cycles of (k+1)//2

# sum_ones = sum over cycles of k//2

# sum_twos = 0

# But the queries give A0, A1, A2 with A0 + A1 + A2 = N.

# So if A2 > 0, we must assign some nodes to 2.

# So we need to adjust the assignments to match the query counts.

# Since 2's reduce the sum, we want to minimize the number of 2's.

# So the problem reduces to:

# Given the fixed counts of zeros and ones from the alternating assignments, can we adjust the assignments to match the query counts?

# If A2 > 0, we must assign some nodes to 2.

# So we need to "convert" some zeros or ones to twos.

# Converting a zero or one to two reduces the sum.

# We need to find the minimal loss in sum when converting nodes from 0 or 1 to 2.

# Let's analyze the loss when converting a node from 0 or 1 to 2.

# For a node in a cycle, changing its value affects the edges adjacent to it.

# Each node has degree 2 in the cycle (two edges).

# Let's consider the loss in sum when changing a node's value from 0 or 1 to 2.

# Let's analyze the loss per node:

# For a node assigned 0 in alternating assignment:

# Its neighbors are assigned 1 (since alternating).

# Edges: (0,1) and (prev_node,0) where prev_node is 1.

# Each edge (0,1) gives 2 points.

# So total contribution of edges adjacent to this node is 2 + 2 = 4.

# If we change this node's value from 0 to 2:

# Edges become (2,1) and (1,2).

# mex(2,1) = 0, mex(1,2) = 0

# So total contribution becomes 0 + 0 = 0.

# Loss = 4.

# For a node assigned 1 in alternating assignment:

# Its neighbors are assigned 0.

# Edges: (1,0) and (0,1), each 2 points, total 4.

# Changing node from 1 to 2:

# Edges become (2,0) and (0,2).

# mex(2,0) = 1, mex(0,2) = 1

# Total 2.

# Loss = 4 - 2 = 2.

# So changing a 0 node to 2 loses 4 points.

# Changing a 1 node to 2 loses 2 points.

# So to minimize loss, we should convert 1 nodes to 2 first, then 0 nodes.

# Now, for each cycle, we know the counts of 0 and 1 nodes:

# zeros = (k+1)//2

# ones = k//2

# For the whole graph:

# total_zeros = sum over cycles of zeros

# total_ones = sum over cycles of ones

# total_twos = 0

# Now, for each query (A0, A1, A2):

# We want to assign A0 zeros, A1 ones, A2 twos.

# We start from the base assignment:

# zeros = total_zeros

# ones = total_ones

# twos = 0

# We need to convert some zeros and ones to twos to get the desired counts.

# Let x = number of ones converted to twos

# Let y = number of zeros converted to twos

# Then:

# A2 = x + y

# A1 = total_ones - x

# A0 = total_zeros - y

# So:

# x = total_ones - A1

# y = total_zeros - A0

# Both x,y >= 0

# Also, x + y = A2

# So check if x,y are integers >= 0 and x + y = A2

# If not possible, answer is 0 (no valid assignment)

# If possible, total loss = 2*x + 4*y

# Base sum = sum over cycles of (2*k if k even else 2*k -1)

# So final answer = base_sum - total_loss

# Implementing this:

# 1. Find cycles and their lengths

# 2. For each cycle, compute zeros = (k+1)//2, ones = k//2, base sum for cycle

# 3. Sum over all cycles to get total_zeros, total_ones, base_sum

# 4. For each query, compute x = total_ones - A1, y = total_zeros - A0

#    If x<0 or y<0 or x + y != A2, print 0

#    Else print base_sum - (2*x + 4*y)

# This is O(N + Q) solution.

# Let's implement it.

visited = [False]*N
cycles = []
for i in range(N):
    if not visited[i]:
        cycle = []
        cur = i
        while not visited[cur]:
            visited[cur] = True
            cycle.append(cur)
            cur = P[cur]-1
        cycles.append(cycle)

total_zeros = 0
total_ones = 0
base_sum = 0

for c in cycles:
    k = len(c)
    zeros = (k+1)//2
    ones = k//2
    total_zeros += zeros
    total_ones += ones
    if k % 2 == 0:
        base_sum += 2*k
    else:
        base_sum += 2*k - 1

for _ in range(Q):
    A0, A1, A2 = map(int, input().split())
    x = total_ones - A1  # ones converted to twos
    y = total_zeros - A0 # zeros converted to twos
    if x < 0 or y < 0 or x + y != A2:
        print(0)
    else:
        loss = 2*x + 4*y
        print(base_sum - loss)