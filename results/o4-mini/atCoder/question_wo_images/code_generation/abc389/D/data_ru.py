import sys
import math

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    R = int(data)
    T = 4 * R * R
    count = 0
    # iterate over i >= 0
    for i in range(R):
        ui = 2 * i + 1
        ui2 = ui * ui
        # we need (2j+1)^2 <= T - ui2, and (2j+1)^2 >= 1, so T - ui2 >= 1
        if ui2 > T - 1:
            break
        rem = T - ui2
        vsq = math.isqrt(rem)
        if vsq < 1:
            continue
        # we need the largest odd v <= vsq
        if vsq & 1:
            v_max = vsq
        else:
            v_max = vsq - 1
        if v_max < 1:
            continue
        j_max = (v_max - 1) // 2
        # multiplicity for i: 1 if i==0 else 2 (for ±i)
        mul_i = 1 if i == 0 else 2
        # sum of multiplicities for j from 0 to j_max:
        # j=0 contributes 1, j>=1 each contributes 2 => total = 1 + 2*j_max
        cnt_j = 1 + 2 * j_max
        count += mul_i * cnt_j

    print(count)

if __name__ == "__main__":
    main()