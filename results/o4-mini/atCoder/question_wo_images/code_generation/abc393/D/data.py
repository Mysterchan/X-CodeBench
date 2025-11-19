import sys
import threading

def main():
    import sys

    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]

    # B[i] = position_of_i-th_one - i
    B = []
    ones_count = 0
    for idx, ch in enumerate(s):
        if ch == '1':
            B.append(idx - ones_count)
            ones_count += 1

    # Find median of B
    k = ones_count
    median = B[k // 2]

    # Compute total cost as sum of absolute deviations from median
    result = 0
    for b in B:
        if b >= median:
            result += b - median
        else:
            result += median - b

    print(result)

if __name__ == "__main__":
    main()