import sys
import threading

def main():
    A = list(map(int, sys.stdin.readline().split()))
    from itertools import permutations
    for B in permutations(A, 3):
        if B[0] * B[1] == B[2]:
            print("Yes")
            return
    print("No")

if __name__ == "__main__":
    main()