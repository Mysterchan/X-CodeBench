def main():
    import sys
    from collections import Counter
    
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    A = data[1]
    
    length = 3 ** N
    result = [A]
    
    # Function to reduce the list based on the majority rule
    def majority_reduce(s):
        reduced = []
        for i in range(0, len(s), 3):
            count = Counter(s[i:i+3])
            reduced.append(max(count, key=lambda x: (count[x], x)))
        return ''.join(reduced)
    
    # Reduce N times to get the final value
    for _ in range(N):
        A = majority_reduce(A)
        result.append(A)
    
    final_value = result[-1]

    # Function to determine the minimum changes to flip the final value
    def min_changes_to_flip(original, desired):
        counts = [0, 0]
        
        # Count the contributions to the final value
        for i in range(0, len(original), 3):
            segment = original[i:i+3]
            count = Counter(segment)
            if count['1'] > count['0']:  # Majority chose '1'
                counts[1] += 1
            else:  # Majority chose '0'
                counts[0] += 1
        
        # Determine what we need to flip the final value
        if desired == '1':
            # To become '0', we need to flip enough '1's that they do not form the majority
            return counts[1]  # We can count '1' majority segments
        else:
            # To become '1', we need to flip enough '0's that they do not form the majority
            return counts[0]  # We can count '0' majority segments
        
    # Determine minimum changes needed
    if final_value == '1':
        result = min_changes_to_flip(data[1], '0')
    else:
        result = min_changes_to_flip(data[1], '1')
    
    print(result)

if __name__ == "__main__":
    main()