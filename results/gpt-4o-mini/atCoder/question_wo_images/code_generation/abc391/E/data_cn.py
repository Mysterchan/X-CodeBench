def majority_counts(b_string):
    counts = []
    for i in range(0, len(b_string), 3):
        segment = b_string[i:i + 3]
        count_0 = segment.count('0')
        count_1 = segment.count('1')
        if count_0 > count_1:
            counts.append('0')
        else:
            counts.append('1')
    return ''.join(counts)

def transform_to_majority(a, n):
    current = a
    for _ in range(n):
        current = majority_counts(current)
    return current

def min_changes_to_flip(a, n):
    initial_value = transform_to_majority(a, n)
    length = len(a)
    required_flips = 0
    
    # Check how many changes are required to flip the final result
    # to its opposite value (0 -> 1 or 1 -> 0)
    target_value = '1' if initial_value == '0' else '0'
    
    for i in range(length):
        modified_a = list(a)
        # Try flipping each bit one by one
        original_bit = modified_a[i]
        modified_a[i] = target_value  # Flip the bit
        
        if transform_to_majority(''.join(modified_a), n) == target_value:
            required_flips += 1
            
    return required_flips

n = int(input().strip())
a = input().strip()
print(min_changes_to_flip(a, n))