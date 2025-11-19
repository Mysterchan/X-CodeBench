mod = 10**9 + 7

import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        total = n * m
        total0 = (total + 1) // 2
        total1 = total - total0

        count_fixed0 = 0
        count_fixed1 = 0
        a_fixed = 0
        c_fixed = 0

        for _ in range(k):
            x = int(data[index])
            y = int(data[index + 1])
            c = int(data[index + 2])
            index += 3
            if (x + y) % 2 == 0:
                count_fixed0 += 1
                a_fixed = (a_fixed + c) % 2
            else:
                count_fixed1 += 1
                c_fixed = (c_fixed + c) % 2

        free0 = total0 - count_fixed0
        free1 = total1 - count_fixed1
        free_count = free0 + free1

        coef0 = total1 % 2
        coef1 = total0 % 2
        R = (coef0 * a_fixed + coef1 * c_fixed) % 2

        if coef0 == 0 and coef1 == 0:
            if R == 0:
                ans = pow(2, free_count, mod)
            else:
                ans = 0
        else:
            if free_count == 0:
                ans = 1 if R == 0 else 0
            else:
                if (coef0 != 0 and free0 > 0) or (coef1 != 0 and free1 > 0):
                    ans = pow(2, free_count - 1, mod)
                else:
                    if R == 0:
                        ans = pow(2, free_count, mod)
                    else:
                        ans = 0
        results.append(str(ans % mod))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
