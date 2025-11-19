import math
import sys

def count_squares(R):
    count = 0
    for i in range(-R, R + 1):
        for j in range(-R, R + 1):
            if (math.sqrt(i**2 + j**2) + 0.5) <= R:
                count += 1
    return count

if __name__ == "__main__":
    R = int(sys.stdin.read().strip())
    result = count_squares(R)
    print(result)