import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    R = int(data[0])
    R2 = 4 * R * R
    # Compute axis count A: maximum i>0 such that square at (i,0) is inside
    M0 = R2 - 1  # 4*R^2 - 1^2
    u0 = math.isqrt(M0)
    if u0 % 2 == 0:
        u0 -= 1
    A = (u0 - 1) // 2

    # Sum non-axis squares: for i=1..A, count j>=1 such that square at (i,j) is inside
    total_j = 0
    for i in range(1, A + 1):
        M = R2 - (2 * i + 1) * (2 * i + 1)
        # M >= 1 for i <= A by construction
        u = math.isqrt(M)
        if u % 2 == 0:
            u -= 1
        j_max = (u - 1) // 2  # maximum j >= 0
        total_j += j_max

    # Total squares = center + axis squares + 4 * non-axis-quadrant squares
    result = 1 + 4 * A + 4 * total_j
    sys.stdout.write(str(result))

if __name__ == "__main__":
    main()