t = int(input())
for _ in range(t):
    n = int(input())
    total_operations = 0
    excess_zeros = 0
    excess_ones = 0
    
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        excess_zeros += max(0, a - c)  # Count how many excess zeros we have
        excess_ones += max(0, b - d)    # Count how many excess ones we have
        
        deficit_zeros = max(0, c - a)   # Count how many zeros we need
        deficit_ones = max(0, d - b)    # Count how many ones we need
        
        total_operations += deficit_zeros + deficit_ones

    # The number of operations is the maximum of excess of zeros and ones
    # because every move can fix only one excess of either type
    print(max(excess_zeros, excess_ones, total_operations // 2))