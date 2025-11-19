import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    for _ in range(t):
        s = int(input[idx])
        k = int(input[idx + 1])
        idx += 2

        if s == k:
            print(k)
            continue
        if s % k == 0:
            print(k)
            continue

        max_power = 0
        for t_turns in range(k):
            sum_t = 0
            for i in range(1, t_turns + 1):
                if i % 2 == 1:
                    term = -(k - i)
                else:
                    term = (k - i)
                sum_t += term

            total_displacement = k + sum_t
            remaining = s - total_displacement
            if remaining < 0:
                continue
            p = k - t_turns
            if p <= 0:
                continue
            if remaining % p != 0:
                continue
            m = remaining // p

            dir_sign = 1 if t_turns % 2 == 0 else -1
            new_pos = total_displacement + m * p * dir_sign

            if new_pos < 0 or new_pos > s:
                continue

            if dir_sign == 1:
                if total_displacement > s:
                    continue
                if total_displacement + m * p > s:
                    continue
            else:
                if total_displacement < 0:
                    continue
                if total_displacement - m * p < 0:
                    continue

            if p > max_power:
                max_power = p

        if max_power == 0:
            print(1)
        else:
            print(max_power)

if __name__ == "__main__":
    main()
