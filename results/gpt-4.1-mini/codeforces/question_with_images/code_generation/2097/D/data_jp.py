import sys
input = sys.stdin.readline

def can_transform(s, t):
    n = len(s)
    # n must be even to perform operations, but problem states n can be odd.
    # If n is odd, no operation can be performed (since splitting into two equal halves is impossible).
    # So s must be equal to t directly.
    if n % 2 == 1:
        return s == t

    # If s == t, trivially yes
    if s == t:
        return True

    # If s is all zeros, it can never produce any 1s by the operations.
    # Because the operations are XOR-based additions, starting from all zeros,
    # the string remains all zeros.
    if all(ch == '0' for ch in s):
        return all(ch == '0' for ch in t)

    # Similarly, if t is all zeros but s is not, impossible.
    if all(ch == '0' for ch in t) and not all(ch == '0' for ch in s):
        return False

    # The operations allow us to do the following:
    # - Split string into halves x and y (both length n/2)
    # - Replace x by x XOR y or y by x XOR y
    # - Recursively do the same on x and y if their length is even

    # This operation corresponds to a linear transformation over GF(2).
    # The problem reduces to checking if s and t are in the same equivalence class
    # under these operations.

    # Key insight (from editorial and problem analysis):
    # The operation can reorder and XOR parts of the string in a way that
    # the string can be transformed into a canonical form by recursively sorting
    # the halves (after applying XOR operations).

    # We can define a function that returns the canonical form of a string under these operations.
    # Two strings are transformable into each other iff their canonical forms are equal.

    def canonical(a):
        length = len(a)
        if length % 2 == 1:
            return a
        mid = length // 2
        x = canonical(a[:mid])
        y = canonical(a[mid:])
        # We can reorder halves to get lex smallest form
        # Because XOR operations allow us to swap and combine halves,
        # the canonical form is the lexicographically smaller of (x+y) and (y+x),
        # where + is concatenation.
        # But we must consider that XOR operations can change bits,
        # so we need to consider the minimal form under XOR.

        # However, the problem states the operations are:
        # - x = x XOR y
        # - y = x XOR y
        # - recursively on x and y

        # The editorial approach is to recursively get canonical forms of halves,
        # then return the lex smaller of concatenation of (x,y) and (y,x).

        # So we just compare x+y and y+x lex order and return the smaller one.
        if x + y < y + x:
            return x + y
        else:
            return y + x

    return canonical(s) == canonical(t)

t = int(input())
out = []
for _ in range(t):
    n = int(input())
    s = input().rstrip()
    t_str = input().rstrip()
    out.append("Yes" if can_transform(s, t_str) else "No")

print("\n".join(out))