import sys
input = sys.stdin.readline

def can_transform(s, t):
    n = len(s)
    # Base case: if strings are equal, return True
    if s == t:
        return True
    # If length is odd and strings differ, no operations can fix it
    if n % 2 == 1:
        return False

    mid = n // 2
    s_left, s_right = s[:mid], s[mid:]
    t_left, t_right = t[:mid], t[mid:]

    # Check if we can transform s to t by:
    # 1) Applying operation 1: x_i = x_i + y_i mod 2 on s_left
    #    This means s_left_new = s_left XOR s_right
    #    So check if s_left XOR s_right == t_left and s_right == t_right
    # 2) Applying operation 2: y_i = x_i + y_i mod 2 on s_right
    #    This means s_right_new = s_left XOR s_right
    #    So check if s_left == t_left and s_right XOR s_left == t_right
    # 3) Applying operation 3: recursively on s_left and s_right independently

    # Convert strings to int lists for XOR
    s_left_int = [int(c) for c in s_left]
    s_right_int = [int(c) for c in s_right]
    t_left_int = [int(c) for c in t_left]
    t_right_int = [int(c) for c in t_right]

    # Operation 1 check
    op1_left = [ (a ^ b) for a,b in zip(s_left_int, s_right_int) ]
    if op1_left == t_left_int and s_right_int == t_right_int:
        return True

    # Operation 2 check
    op2_right = [ (a ^ b) for a,b in zip(s_left_int, s_right_int) ]
    if s_left_int == t_left_int and op2_right == t_right_int:
        return True

    # Operation 3: recursively check both halves
    # Only if both halves have even length or length 1 (base case)
    # Since length is even, halves are either even or 1
    return can_transform(s_left, t_left) and can_transform(s_right, t_right)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    t_str = input().strip()
    print("Yes" if can_transform(s, t_str) else "No")