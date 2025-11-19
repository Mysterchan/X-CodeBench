def majority_change(n, A):
    length = 3 ** n
    
    def majority_count(start, end):
        count_0 = count_1 = 0
        for i in range(start, end):
            if A[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
        return count_0, count_1
    
    def calculate_final_string(A):
        current_length = len(A)
        while current_length > 1:
            next_length = current_length // 3
            next_A = []
            for i in range(next_length):
                count_0, count_1 = majority_count(3 * i, 3 * i + 3)
                next_A.append('0' if count_0 > count_1 else '1')
            A = ''.join(next_A)
            current_length = next_length
        return A[0]
    
    final_value = calculate_final_string(A)
    
    target_value = '0' if final_value == '1' else '1'
    
    def min_changes_needed(n, A, target_value):
        change_count = 0
        length = 3 ** n
        indexes_to_change = []
        
        for i in range(0, length, 3):
            count_0, count_1 = majority_count(i, i + 3)
            current_majority = '0' if count_0 > count_1 else '1'
            if current_majority != target_value:
                if count_0 > count_1:
                    needed_changes = (count_0 - count_1 + 1) // 2
                else:
                    needed_changes = (count_1 - count_0 + 1) // 2
                change_count += needed_changes
            else:
                fail_case_needed = max(0, (count_1 + 1) // 2)
                change_count += fail_case_needed
        
        return change_count
    
    return min_changes_needed(n, A, target_value)

# Accept input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
A = ''.join(data[1:])

# Compute the result
result = majority_change(N, A)

# Output the result
print(result)