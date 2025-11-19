def can_make_equal_sum(N, A, B):
    # Calculate the total sum of known values in A and B
    sum_A = sum(x for x in A if x != -1)
    sum_B = sum(x for x in B if x != -1)
    
    # Count the number of -1s in A and B
    count_A_neg1 = A.count(-1)
    count_B_neg1 = B.count(-1)
    
    # Total number of -1s
    total_neg1 = count_A_neg1 + count_B_neg1
    
    # The target sum for each pair A_i + B_i
    # We need to find a target sum that can be achieved
    # The total sum of A and B must be equal to N * target_sum
    # target_sum = (sum_A + sum_B + x) / N where x is the sum of all replacements
    
    # The minimum target sum we can achieve
    min_target_sum = (sum_A + sum_B) // N
    
    # The maximum target sum we can achieve
    max_target_sum = (sum_A + sum_B + total_neg1 * (10**9)) // N
    
    # Check if we can find a valid target sum
    for target_sum in range(min_target_sum, max_target_sum + 1):
        # Calculate the total needed to reach this target sum
        needed_A = 0
        needed_B = 0
        
        for i in range(N):
            if A[i] == -1:
                needed_A += target_sum
            else:
                needed_A += target_sum - A[i]
                
            if B[i] == -1:
                needed_B += target_sum
            else:
                needed_B += target_sum - B[i]
        
        # Check if we can satisfy the needed values with the available -1s
        if needed_A <= count_A_neg1 * (10**9) and needed_B <= count_B_neg1 * (10**9):
            return "Yes"
    
    return "No"

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
A = list(map(int, data[1].split()))
B = list(map(int, data[2].split()))

# Output the result
print(can_make_equal_sum(N, A, B))