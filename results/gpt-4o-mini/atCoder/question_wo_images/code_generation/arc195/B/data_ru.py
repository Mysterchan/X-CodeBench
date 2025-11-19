def can_make_equal_sums(N, A, B):
    total_A = sum(x for x in A if x != -1)
    total_B = sum(x for x in B if x != -1)
    
    count_A_neg = A.count(-1)
    count_B_neg = B.count(-1)
    
    # Calculate the total number of elements that can be adjusted
    total_neg = count_A_neg + count_B_neg
    
    # The target sum for each pair A_i + B_i
    target_sum = (total_A + total_B) / N
    
    # Check if target_sum is an integer
    if target_sum != int(target_sum):
        return "No"
    
    target_sum = int(target_sum)
    
    # Calculate the total amount needed to reach the target sum
    needed_A = sum(max(0, target_sum - b) for b in B if b != -1)
    needed_B = sum(max(0, target_sum - a) for a in A if a != -1)
    
    # Check if we have enough -1s to cover the needed amounts
    if needed_A <= count_A_neg and needed_B <= count_B_neg:
        return "Yes"
    
    return "No"

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
A = list(map(int, data[1:N+1]))
B = list(map(int, data[N+1:2*N+1]))

print(can_make_equal_sums(N, A, B))