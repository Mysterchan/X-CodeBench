def can_place_rabbits(n, s):
    if '000' in s:  # If there are at least 3 consecutive empty pots
        return "YES"
    
    for i in range(1, n - 1):
        if s[i] == '0' and s[i - 1] == '0' and s[i + 1] == '0':
            return "YES"
    
    for i in range(n):
        if s[i] == '0':
            if i > 0 and s[i - 1] == '0':
                return "NO"
            if i < n - 1 and s[i + 1] == '0':
                return "NO"
    
    return "YES"

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    s = input().strip()
    results.append(can_place_rabbits(n, s))

print("\n".join(results))