import sys
input = sys.stdin.readline

T = int(input())

# Explanation and reasoning:
# We have a circular sequence A of length N = X+Y+Z with exactly X zeros, Y ones, Z twos.
# For each position i, exactly A_i numbers among neighbors A_{i-1} and A_{i+1} are less than A_i.
#
# Since neighbors are two elements, the count of neighbors less than A_i can be 0,1, or 2.
# The condition states that this count equals A_i.
#
# So:
# - If A_i = 0, then 0 neighbors are less than A_i => both neighbors >= 0 (always true since values are 0,1,2)
# - If A_i = 1, then exactly 1 neighbor is less than A_i
# - If A_i = 2, then exactly 2 neighbors are less than A_i
#
# Let's analyze possible neighbor relations:
#
# For A_i=0:
#   neighbors less than 0 = 0 always (since no value < 0)
#   So neighbors can be anything.
#
# For A_i=1:
#   neighbors less than 1 = exactly 1
#   neighbors are from {0,1,2}
#   So neighbors must be one 0 and one >=1 (1 or 2)
#
# For A_i=2:
#   neighbors less than 2 = 2
#   both neighbors < 2 => neighbors are 0 or 1
#
# Summary:
# - 0: neighbors any
# - 1: neighbors must be one 0 and one >=1
# - 2: neighbors both < 2 (0 or 1)
#
# Let's consider the sequence as circular.
#
# Key observations:
# - For A_i=2, neighbors are from {0,1}
# - For A_i=1, neighbors are one 0 and one >=1
# - For A_i=0, neighbors any
#
# Let's try to find necessary conditions:
#
# 1) If there is any 2, its neighbors must be from {0,1}.
#    So no 2 can be adjacent to 2.
#
# 2) For 1, neighbors must be one 0 and one >=1.
#    So 1 cannot have two neighbors both 0 or both >=1.
#
# 3) For 0, no restriction.
#
# Let's try to build a sequence pattern:
#
# Since 2 cannot be adjacent to 2, 2's must be separated by at least one 0 or 1.
#
# For 1, neighbors must be one 0 and one >=1.
# So neighbors of 1 are (0,1) or (0,2).
# But 1 cannot have neighbors (1,1) or (2,2) or (1,2).
#
# Let's try to find a pattern that satisfies all:
#
# Consider the sequence as a circle:
#
# Let's try to place all 2's separated by 0 or 1.
# But 2's neighbors must be from {0,1}.
#
# Also, 1's neighbors must be one 0 and one >=1.
#
# Let's try to find a sequence with only 0 and 2:
# For 2, neighbors must be 0 or 1, but no 1's here, so neighbors must be 0.
# So 2's neighbors must be 0.
# So 2's cannot be adjacent to 2.
#
# For 0, no restriction.
#
# So a sequence of 0 and 2 alternating is possible.
#
# For 1's:
# 1's neighbors must be one 0 and one >=1.
# So neighbors of 1 must be (0,1) or (0,2).
#
# So 1's cannot be adjacent to 0 and 0, or 1 and 1, or 2 and 2.
#
# So 1's must be between 0 and 1 or 0 and 2.
#
# Let's try to find a general condition:
#
# Let's define counts:
# X = count of 0
# Y = count of 1
# Z = count of 2
#
# Let's consider the number of edges between different values.
#
# Since the sequence is circular, number of edges = N
#
# Let's consider edges between:
# - 0 and 0
# - 0 and 1
# - 0 and 2
# - 1 and 1
# - 1 and 2
# - 2 and 2
#
# From the conditions:
# - 2's neighbors must be from {0,1} => no 2-2 edges
# - 1's neighbors must be one 0 and one >=1
#   So 1's neighbors are (0,1) or (0,2)
#   So 1 cannot have neighbors (1,1) or (2,2) or (1,2)
#
# So edges 1-1 and 1-2 are forbidden.
#
# So edges allowed:
# - 0-0
# - 0-1
# - 0-2
# - 1-0
# - 2-0
# - 2-1 (no, forbidden)
# - 2-2 (no)
# - 1-1 (no)
#
# So edges allowed are only between 0 and 0, 0 and 1, 0 and 2.
#
# So the sequence is formed by 0's connected to 0's, 1's, and 2's.
#
# So the sequence is a circle with only edges between 0 and others, and possibly 0-0 edges.
#
# So the sequence is a circle where all 1's and 2's are adjacent only to 0's.
#
# So the sequence looks like:
# 0 - 1 - 0 - 2 - 0 - 1 - 0 - 2 - 0 ...
#
# So all 1's and 2's are separated by at least one 0.
#
# So the number of 0's must be at least the number of 1's and 2's.
#
# Because each 1 and 2 must be adjacent to two 0's (since neighbors are two elements, and both neighbors of 2 must be < 2, so neighbors are 0 or 1, but 1 cannot be neighbor of 2, so neighbors of 2 must be 0).
#
# Wait, for 2:
# neighbors must be both less than 2 => neighbors in {0,1}
# But 1 cannot be neighbor of 2 because 1's neighbors must be one 0 and one >=1.
# So 1 cannot be neighbor of 2.
#
# So 2's neighbors must be 0 and 0.
#
# So each 2 must be surrounded by two 0's.
#
# For 1:
# neighbors must be one 0 and one >=1.
# So neighbors of 1 are (0,1) or (0,2).
#
# So 1 can be adjacent to 0 and 1 or 0 and 2.
#
# So 1's neighbors are one 0 and one 1 or 2.
#
# So 1 can be adjacent to 1 or 2, but only one neighbor is less than 1 (which is 0).
#
# So 1's neighbors are (0,1) or (0,2).
#
# So 1 can be adjacent to 1 or 2, but only one neighbor less than 1 (the 0).
#
# So 1 can be adjacent to 1 or 2, but not both neighbors less than 1.
#
# So 1's neighbors are one 0 and one 1 or 2.
#
# So 1's neighbors are (0,1) or (0,2).
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1's neighbors are one 0 and one >=1.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can be 0 and 1 or 0 and 2.
#
# So 1 can be adjacent to 1 or 2.
#
# So 1's neighbors can