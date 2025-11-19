import sys
input = sys.stdin.readline

def run_length_encode(arr):
    res = []
    prev = arr[0]
    count = 1
    for v in arr[1:]:
        if v == prev:
            count += 1
        else:
            res.append((prev, count))
            prev = v
            count = 1
    res.append((prev, count))
    return res

def normalize(rle, x, y):
    # Merge runs of same value separated by runs of length < x or y as per the operation
    # Actually, the operation swaps blocks of 0^X 1^Y <-> 1^Y 0^X
    # So runs of length < x or y cannot be swapped.
    # The key insight is that runs of length >= x or y can be rearranged arbitrarily.
    # So we reduce runs of length >= x or y to length x or y respectively,
    # and merge adjacent runs of same value.
    # This normalization is unique and can be used to compare S and T.

    # For each run:
    # - if value == 0 and length >= x, set length = x
    # - if value == 1 and length >= y, set length = y
    # - else keep length as is

    normalized = []
    for val, length in rle:
        if val == 0 and length >= x:
            length = x
        elif val == 1 and length >= y:
            length = y
        # merge with previous if same val
        if normalized and normalized[-1][0] == val:
            normalized[-1] = (val, normalized[-1][1] + length)
        else:
            normalized.append((val, length))
    return normalized

def main():
    n, x, y = map(int, input().split())
    s = list(map(int, input().strip()))
    t = list(map(int, input().strip()))

    # If s == t, answer Yes immediately
    if s == t:
        print("Yes")
        return

    # Run length encode s and t
    rle_s = run_length_encode(s)
    rle_t = run_length_encode(t)

    # Normalize both
    norm_s = normalize(rle_s, x, y)
    norm_t = normalize(rle_t, x, y)

    # If normalized forms differ in length, no
    if len(norm_s) != len(norm_t):
        print("No")
        return

    # Check each run matches in value and length
    for (vs, ls), (vt, lt) in zip(norm_s, norm_t):
        if vs != vt or ls != lt:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()