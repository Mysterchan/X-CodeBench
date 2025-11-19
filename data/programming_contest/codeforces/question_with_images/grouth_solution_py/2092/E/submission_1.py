MOD = 10**9 + 7

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
        total_ones = 2 * (n + m) - 8

        R = 0
        fixed_ones = 0
        for _ in range(k):
            x = int(data[index])
            y = int(data[index + 1])
            c = int(data[index + 2])
            index += 3
            coeff = 0
            if x == 1:
                coeff += 1
            if x == n:
                coeff += 1
            if y == 1:
                coeff += 1
            if y == m:
                coeff += 1
            coeff %= 2
            R = (R + coeff * c) % 2
            if coeff == 1:
                fixed_ones += 1

        free_ones = total_ones - fixed_ones
        total_free = n * m - k

        if free_ones > 0:
            ans = pow(2, total_free - 1, MOD)
        else:
            if R % 2 == 0:
                ans = pow(2, total_free, MOD)
            else:
                ans = 0
        results.append(str(ans))

    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()

