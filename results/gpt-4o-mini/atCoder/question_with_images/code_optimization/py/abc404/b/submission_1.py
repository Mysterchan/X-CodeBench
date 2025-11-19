n = int(input())
s = [input().strip() for _ in range(n)]
t = [input().strip() for _ in range(n)]

def count_diff(s, t):
    return sum(1 for i in range(n) for j in range(n) if s[i][j] != t[i][j])

min_operations = float('inf')

# Original orientation
min_operations = min(min_operations, count_diff(s, t))

# Rotate 90 degrees three times and compare
for _ in range(3):
    s = [''.join(s[n - 1 - j][i] for j in range(n)) for i in range(n)]
    min_operations = min(min_operations, count_diff(s, t))

print(min_operations)