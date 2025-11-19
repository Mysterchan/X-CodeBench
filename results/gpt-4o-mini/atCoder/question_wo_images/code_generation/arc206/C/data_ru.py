def count_good_sequences(N, A):
    MOD = 998244353
    
    # Count the number of -1s and the set of fixed values
    count_neg = 0
    fixed_values = set()
    
    for value in A:
        if value == -1:
            count_neg += 1
        else:
            fixed_values.add(value)
    
    # The number of unique values that can be used to fill -1s
    unique_values = N - len(fixed_values)
    
    # If there are more -1s than unique values, it's impossible to fill them
    if count_neg > unique_values:
        return 0
    
    # Calculate the number of ways to fill the -1s
    # We can choose any of the unique values for each -1
    ways = 1
    for i in range(count_neg):
        ways = (ways * (unique_values - i)) % MOD
    
    return ways

# Read input
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Get the result and print it
result = count_good_sequences(N, A)
print(result)