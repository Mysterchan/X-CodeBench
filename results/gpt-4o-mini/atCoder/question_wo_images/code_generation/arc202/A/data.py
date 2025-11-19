def min_insertions_to_good_sequence(test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        freq = {}
        
        # Count frequencies of each number in the sequence
        for x in a:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        # Calculate maximum number of merges possible based on frequencies
        inserts = 0
        
        # This set keeps track of how many times we've made a value `x` available
        current_available = 0
        
        # Process numbers - since they need to be processed in sorted order
        for x in sorted(freq.keys()):
            current_available += freq[x]
            # If current_available is odd, we need one more to convert to even
            if current_available % 2 == 1:
                inserts += 1
            
            # All pairs can merge to produce current_available // 2
            current_available //= 2
        
        results.append(inserts)
    
    return results


# Read the input
import sys
input = sys.stdin.read

def main():
    lines = input().splitlines()
    T = int(lines[0])
    
    test_cases = []
    index = 1
    for _ in range(T):
        N = int(lines[index])
        A = list(map(int, lines[index + 1].split()))
        test_cases.append((N, A))
        index += 2
    
    results = min_insertions_to_good_sequence(test_cases)
    
    # Output the results
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

main()