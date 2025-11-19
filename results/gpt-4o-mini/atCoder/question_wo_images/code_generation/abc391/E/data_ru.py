def majority_change_needed(N, A):
    def majority_value(segment):
        return 1 if segment.count('1') > segment.count('0') else 0

    length = 3 ** N
    A_prime = A

    for _ in range(N):
        next_length = len(A_prime) // 3
        new_A_prime = ''.join(majority_value(A_prime[i:i+3]) for i in range(0, len(A_prime), 3))
        A_prime = new_A_prime

    target_value = A_prime

    changes_needed = 0
    for i in range(3 ** N):
        # Check what changes would happen if we changed A[i]
        original = A[i]
        modified_A = list(A)
        modified_A[i] = '1' if original == '0' else '0'
        
        modified_A_prime = ''.join(
            ''.join(
                majority_value(modified_A[j:j+3]) 
                for j in range(0, length, 3)
            )
            for _ in range(N)
        )
        
        if modified_A_prime != target_value:
            changes_needed += 1

    return changes_needed

import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = data[1]

result = majority_change_needed(N, A)
print(result)