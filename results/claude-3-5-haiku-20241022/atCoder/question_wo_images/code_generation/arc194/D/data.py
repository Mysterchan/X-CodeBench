from collections import deque

def is_valid(s):
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def reverse_substring(s, l, r):
    # Convert to list for mutability
    s_list = list(s)
    # Reverse and flip parentheses
    for i in range(l, r + 1):
        mirror_pos = l + r - i
        if s[mirror_pos] == '(':
            s_list[i] = ')'
        else:
            s_list[i] = '('
    return ''.join(s_list)

def solve(n, s):
    visited = {s}
    queue = deque([s])
    
    while queue:
        current = queue.popleft()
        
        # Try all possible valid substrings
        for l in range(n):
            for r in range(l + 1, n):
                substring = current[l:r+1]
                if is_valid(substring):
                    # Apply the operation
                    new_s = reverse_substring(current, l, r)
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
    
    return len(visited)

# Read input
n = int(input())
s = input().strip()

# Solve and print result
result = solve(n, s)
print(result % 998244353)