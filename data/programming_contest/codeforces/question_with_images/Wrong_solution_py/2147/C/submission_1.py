import sys

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        s = data[index].strip(); index += 1
        if n == 0:
            results.append("YES")
            continue

        safe = [False] * n
        for i in range(n):
            if s[i] == '0':
                left_one = (i - 1 >= 0) and (s[i-1] == '1')
                right_one = (i + 1 < n) and (s[i+1] == '1')
                safe[i] = not (left_one and right_one)

        segments = []
        i = 0
        while i < n:
            if s[i] == '0':
                j = i
                while j < n and s[j] == '0':
                    j += 1
                segments.append((i, j-1))
                i = j
            else:
                i += 1

        valid = True
        for (L, R) in segments:
            length = R - L + 1
            if length == 1:
                left_one = (L - 1 >= 0) and (s[L-1] == '1')
                right_one = (R + 1 < n) and (s[R+1] == '1')
                if left_one and right_one:
                    j = L
                    found = False
                    while j >= 0:
                        if safe[j]:
                            found = True
                            break
                        j -= 2
                        if j < 0:
                            break
                        if s[j] != '0':
                            break
                    if not found:
                        valid = False
        results.append("YES" if valid else "NO")

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
