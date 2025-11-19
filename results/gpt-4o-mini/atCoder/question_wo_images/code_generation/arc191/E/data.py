def count_winning_ways(N, X, Y, bags):
    MOD = 998244353
    
    # Calculate the number of winning bags for Takahashi
    winning_bags = 0
    
    for A, B in bags:
        if A > 0 or (B > 0 and (B - 1) // Y < (A + (B - 1) // Y) // X):
            winning_bags += 1
    
    # The number of ways Takahashi can choose bags is 2^winning_bags
    # We need to compute this modulo MOD
    if winning_bags == 0:
        return 0
    
    result = pow(2, winning_bags, MOD)
    
    return result

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N, X, Y = map(int, data[0].split())
bags = [tuple(map(int, line.split())) for line in data[1:N+1]]

# Get the result and print it
result = count_winning_ways(N, X, Y, bags)
print(result)