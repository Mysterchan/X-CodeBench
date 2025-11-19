import sys

def can_transform(s, t):
    # Check if both strings have at least one '1'
    return (s.count('1') > 0) == (t.count('1') > 0)

def solve():
    n = int(sys.stdin.readline())
    s_str = sys.stdin.readline().strip()
    t_str = sys.stdin.readline().strip()
    
    if can_transform(s_str, t_str):
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")

num_test_cases = int(sys.stdin.readline())
for _ in range(num_test_cases):
    solve()