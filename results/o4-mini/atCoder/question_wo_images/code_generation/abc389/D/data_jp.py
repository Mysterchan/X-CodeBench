import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    R = int(data[0])
    R2 = R * R
    total = 0
    for i in range(R):
        ai = 2 * i + 1
        fourS = 4 * R2 - ai * ai
        if fourS < 1:
            break
        m = math.isqrt(fourS)
        jmax = (m - 1) // 2
        if i == 0:
            total += 1 + 2 * jmax
        else:
            total += 2 + 4 * jmax
    sys.stdout.write(str(total))

if __name__ == "__main__":
    main()