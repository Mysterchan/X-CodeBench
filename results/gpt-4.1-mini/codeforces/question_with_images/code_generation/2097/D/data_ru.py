import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def can_transform(s, t):
    n = len(s)
    if s == t:
        return True
    if n % 2 == 1:
        return False
    half = n // 2
    s1, s2 = s[:half], s[half:]
    t1, t2 = t[:half], t[half:]
    # Check if can transform by recursive splitting
    # or by applying one of the two xor operations on halves
    # The operations:
    # 1) x_i = x_i + y_i mod 2
    # 2) y_i = x_i + y_i mod 2
    # or recursively transform halves independently

    # Try recursive transform on halves independently
    if can_transform(s1, t1) and can_transform(s2, t2):
        return True

    # Try operation 1: x = x + y mod 2, y unchanged
    # So s1' = s1 ^ s2, s2' = s2
    s1_op1 = ''.join(str((int(a) ^ int(b))) for a,b in zip(s1, s2))
    if s1_op1 == t1 and s2 == t2:
        return True

    # Try operation 2: y = x + y mod 2, x unchanged
    # So s1' = s1, s2' = s1 ^ s2
    s2_op2 = ''.join(str((int(a) ^ int(b))) for a,b in zip(s1, s2))
    if s1 == t1 and s2_op2 == t2:
        return True

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    t_str = input().strip()
    print("Yes" if can_transform(s, t_str) else "No")