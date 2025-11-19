import sys
input = sys.stdin.readline

def can_transform(s, t):
    n = len(s)
    if s == t:
        return True
    if n % 2 == 1:
        return False
    mid = n // 2
    s1, s2 = s[:mid], s[mid:]
    t1, t2 = t[:mid], t[mid:]
    # Check if can transform by applying operation 3 (recursive on halves)
    if can_transform(s1, t1) and can_transform(s2, t2):
        return True
    # Check if can transform by operation 1: x_i = (x_i + y_i) mod 2
    # That means s1 = s1 + s2 mod 2, s2 unchanged
    # So t1 = s1 ^ s2, t2 = s2
    if all((int(s1[i]) ^ int(s2[i])) == int(t1[i]) for i in range(mid)) and t2 == s2:
        return True
    # Check if can transform by operation 2: y_i = (x_i + y_i) mod 2
    # That means s2 = s1 + s2 mod 2, s1 unchanged
    # So t1 = s1, t2 = s1 ^ s2
    if t1 == s1 and all((int(s1[i]) ^ int(s2[i])) == int(t2[i]) for i in range(mid)):
        return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    t_str = input().strip()
    print("Yes" if can_transform(s, t_str) else "No")