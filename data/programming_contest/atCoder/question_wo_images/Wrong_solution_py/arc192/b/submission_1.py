import sys
import os

IS_LOCAL = os.environ.get("LOCAL") == "true"

def debug(*args, sep=" ", end="\n", flush=False) -> None:
    if IS_LOCAL:
        print(*args, sep=sep, end=end, file=sys.stderr, flush=flush)

def yn(flg: bool) -> bool:
    print('Yes' if flg else 'No')
    return flg

def main():
    readline = sys.stdin.readline

    int(input())
    A = list(map(int, readline().split()))
    ev, od = 0, 0
    for a in A:
        if a % 2 == 0:
            ev += 1
        else:
            od += 1
    if ev * 2 + od in (1, 3, 4, 6):
        print('Fennec')
    else:
        print('Snuke')

if __name__ == "__main__":
    main()