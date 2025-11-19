def can_take_picture(test_cases):
    results = []
    for s in test_cases:
        n = len(s)
        is_possible = True
        
        for i in range(n):
            if s[i] == '0':
                # When we find an empty pot
                if (i > 0 and s[i - 1] == '0') or (i < n - 1 and s[i + 1] == '0'):
                    # Check if left and right pots are empty
                    is_possible = False
                    break
        results.append("YES" if is_possible else "NO")
    
    return results

import sys
input = sys.stdin.read
data = input().splitlines()
t = int(data[0])
test_cases = [data[i*2 + 2] for i in range(t)]
result = can_take_picture(test_cases)
print("\n".join(result))