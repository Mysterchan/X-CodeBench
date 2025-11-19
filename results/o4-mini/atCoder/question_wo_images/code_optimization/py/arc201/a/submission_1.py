#!/usr/bin/env python3
import sys
import threading
def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    T = int(next(it))
    out = []
    for _ in range(T):
        n = int(next(it))
        s1 = 0  # sum of min(A_i, B_i)
        s2 = 0  # sum of min(B_i, C_i)
        s3 = 0  # sum of min(B_i, A_i + C_i)
        for i in range(n):
            a = int(next(it)); b = int(next(it)); c = int(next(it))
            # Div1 capacity
            if a < b:
                s1 += a
            else:
                s1 += b
            # Div2 capacity
            if b < c:
                s2 += b
            else:
                s2 += c
            # total medium capacity across both types
            ac = a + c
            if b < ac:
                s3 += b
            else:
                s3 += ac
        # maximum K is min(s1, s2, floor(s3/2))
        k = s3 >> 1
        if k > s1:
            k = s1
        if k > s2:
            k = s2
        out.append(str(k))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()