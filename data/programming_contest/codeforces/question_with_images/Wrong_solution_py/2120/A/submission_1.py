import sys
import math

def can_form_square(l1, b1, l2, b2, l3, b3):
    total_area = l1 * b1 + l2 * b2 + l3 * b3

    S_float = math.sqrt(total_area)
    S = int(S_float)

    if S * S != total_area:
        return "NO"

    def check_fit(l_rem, b_rem, l_a, b_a, l_b, b_b):
        if (b_a == b_rem and b_b == b_rem) and (l_a + l_b == l_rem):
            return True

        if (l_a == l_rem and l_b == l_rem) and (b_a + b_b == b_rem):
            return True

        return False




    if (l1 == S and l2 == S and l3 == S) and (b1 + b2 + b3 == S):
        return "YES"

    if (b1 == S and b2 == S and b3 == S) and (l1 + l2 + l3 == S):
        return "YES"


    if l1 == S and b1 < S:
        l_rem = S
        b_rem = S - b1

        if check_fit(l_rem, b_rem, l2, b2, l3, b3):
            return "YES"

    if b1 == S and l1 < S:
        l_rem = S
        b_rem = S - l1
        if check_fit(l_rem, b_rem, l2, b2, l3, b3):
            return "YES"

    return "NO"


def main():
    try:
        data = sys.stdin.read().split()
    except:
        return

    if not data:
        return

    try:
        t = int(data[0])
    except:
        return

    results = []

    for i in range(t):
        start_index = 1 + i * 6

        if start_index + 6 > len(data):
            break

        try:
            dims = [int(x) for x in data[start_index : start_index + 6]]
            l1, b1, l2, b2, l3, b3 = dims

            results.append(can_form_square(l1, b1, l2, b2, l3, b3))
        except ValueError:
            continue

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()
