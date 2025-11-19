def process_queries(queries):
    removed_multiples = set()
    results = []
    
    for A, B in queries:
        # Remove multiples of A
        for multiple in range(A, 10**9 + 1, A):
            removed_multiples.add(multiple)
        
        # Find the B-th smallest number not in removed_multiples
        count = 0
        current_number = 1
        
        while count < B:
            if current_number not in removed_multiples:
                count += 1
                if count == B:
                    results.append(current_number)
            current_number += 1
            
    return results

import sys
input = sys.stdin.read

data = input().splitlines()
Q = int(data[0])
queries = [tuple(map(int, line.split())) for line in data[1:Q + 1]]

results = process_queries(queries)
print('\n'.join(map(str, results)))