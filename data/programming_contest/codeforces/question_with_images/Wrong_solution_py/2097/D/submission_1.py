import sys

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def apply_T1(s):
    n = len(s)
    mid = n // 2
    left = s[:mid]
    right = s[mid:]
    new_left = ''.join('1' if left[i] != right[i] else '0' for i in range(mid))
    return new_left + right

def apply_T2(s):
    n = len(s)
    mid = n // 2
    left = s[:mid]
    right = s[mid:]
    new_right = ''.join('1' if left[i] != right[i] else '0' for i in range(mid))
    return left + new_right

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        s = data[index].strip(); index += 1
        t_str = data[index].strip(); index += 1

        if n % 2 != 0:
            if s == t_str:
                results.append("Yes")
            else:
                results.append("No")
        else:
            if is_power_of_two(n):
                if all(ch == '0' for ch in s):
                    if all(ch == '0' for ch in t_str):
                        results.append("Yes")
                    else:
                        results.append("No")
                else:
                    if all(ch == '0' for ch in t_str):
                        results.append("No")
                    else:
                        results.append("Yes")
            else:
                orbit = set()
                orbit.add(s)
                s1 = apply_T1(s)
                s2 = apply_T2(s)
                s3 = apply_T1(s2)
                s4 = apply_T2(s1)
                s5 = apply_T1(s4)
                orbit.update([s1, s2, s3, s4, s5])
                if t_str in orbit:
                    results.append("Yes")
                else:
                    results.append("No")

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
