import sys
input = lambda: sys.stdin.readline().rstrip()
na = lambda: list(map(int, input().split()))

def normalize(s, x, y):
    s = list(s)
    n = len(s)
    changed = True
    
    while changed:
        changed = False
        i = 0
        while i <= n - x - y:
            # Check for Operation A pattern: X zeros followed by Y ones
            if all(s[j] == 0 for j in range(i, i + x)) and \
               all(s[j] == 1 for j in range(i + x, i + x + y)):
                # Apply Operation A
                for j in range(i, i + y):
                    s[j] = 1
                for j in range(i + y, i + y + x):
                    s[j] = 0
                changed = True
                i += 1
            else:
                i += 1
    
    return s

n, x, y = na()
s = input()
t = input()

s_norm = normalize(s, x, y)
t_norm = normalize(t, x, y)

if s_norm == t_norm:
    print("Yes")
else:
    print("No")