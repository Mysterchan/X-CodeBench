def count_good_sequences(N, A):
    MOD = 998244353

    # Count the number of -1s and the set of fixed values
    count_neg_one = 0
    fixed_values = set()
    
    for value in A:
        if value == -1:
            count_neg_one += 1
        else:
            fixed_values.add(value)

    # The number of unique values that can be used to fill -1s
    available_values = N - len(fixed_values)

    # If there are no -1s, we need to check if the current sequence is good
    if count_neg_one == 0:
        # Check if the sequence is good
        def is_good_sequence(seq):
            for l in range(N):
                for r in range(l, N):
                    # Check if there exists an x in [l, r] such that the condition holds
                    found = False
                    for x in range(l, r + 1):
                        # Create a set to track connected components
                        connected = set()
                        for i in range(l, r + 1):
                            if i != x:
                                connected.add(i)
                                connected.add(seq[i])
                        if len(connected) == (r - l + 1):
                            found = True
                            break
                    if not found:
                        return False
            return True

        if is_good_sequence(A):
            return 1
        else:
            return 0

    # If there are -1s, we can fill them with any of the available values
    # The number of ways to fill the -1s is available_values^count_neg_one
    result = pow(available_values, count_neg_one, MOD)
    return result

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = list(map(int, data[1:]))

# Get the result and print it
result = count_good_sequences(N, A)
print(result)