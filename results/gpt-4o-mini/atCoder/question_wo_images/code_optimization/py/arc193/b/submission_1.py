N = int(input())
s = input()
P = 998244353

# Count the number of 1's in the string
num_ones = s.count('1')
num_zeros = N - num_ones

# The total configurations derived from ones
result = (pow(2, num_ones, P) * (num_zeros + 1)) % P

# Output the result
print(result)