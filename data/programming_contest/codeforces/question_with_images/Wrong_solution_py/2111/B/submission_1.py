def check_base_two_squares(a, b, w, l):
    if w >= a and l >= a + b:
        return True
    if w >= a + b and l >= a:
        return True
    return False

import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        n = int(data[index]); m = int(data[index+1]); index += 2
        boxes = []
        for i in range(m):
            w = int(data[index]); l = int(data[index+1]); h = int(data[index+2]); index += 3
            boxes.append((w, l, h))

        fib = [1, 2]
        for i in range(2, n):
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)

        total_sum = sum(fib)

        if n == 1:
            res = []
            for (w, l, h) in boxes:
                if min(w, l) >= 1 and h >= 1:
                    res.append('1')
                else:
                    res.append('0')
            output_lines.append(''.join(res))
        elif n == 2:
            a = max(fib)
            b = min(fib)
            res = []
            for (w, l, h) in boxes:
                if (min(w, l) >= a and h >= total_sum) or (check_base_two_squares(a, b, w, l) and h >= b):
                    res.append('1')
                else:
                    res.append('0')
            output_lines.append(''.join(res))
        else:
            a = fib[-1]
            b = fib[-2]
            remaining = fib[:-2]
            total = a + b + sum(remaining)
            dp = [False] * (total + 1)
            dp[a] = True

            for r in remaining:
                new_dp = [False] * (total + 1)
                for j in range(total + 1):
                    if dp[j]:
                        new_dp[j] = True
                        if j + r <= total:
                            new_dp[j + r] = True
                dp = new_dp

            H2 = total
            for j in range(total + 1):
                if dp[j]:
                    max_load = max(j, total - j)
                    if max_load < H2:
                        H2 = max_load

            res = []
            for (w, l, h) in boxes:
                if (min(w, l) >= a and h >= total_sum) or (check_base_two_squares(a, b, w, l) and h >= H2):
                    res.append('1')
                else:
                    res.append('0')
            output_lines.append(''.join(res))

    print("\n".join(output_lines))

if __name__ == "__main__":
    main()
