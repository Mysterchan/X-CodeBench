import sys

def main():
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n, x = map(int, data[index].split())
        index += 1
        s = data[index].strip()
        index += 1

        left_clear = True
        for i in range(0, x-1):
            if s[i] == '#':
                left_clear = False
                break

        right_clear = True
        for i in range(x, n):
            if s[i] == '#':
                right_clear = False
                break

        if left_clear or right_clear:
            results.append("1")
        else:
            results.append("2")

    print("\n".join(results))

if __name__ == "__main__":
    main()
