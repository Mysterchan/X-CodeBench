import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    last_pos = dict()
    min_len = float('inf')

    for i, val in enumerate(A):
        if val in last_pos:
            length = i - last_pos[val] + 1
            if length < min_len:
                min_len = length
        last_pos[val] = i

    print(min_len if min_len != float('inf') else -1)

if __name__ == "__main__":
    main()