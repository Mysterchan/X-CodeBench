import sys
import bisect

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    total = 0
    for i in range(N):
        # A[i] の半分以下の最大値を探す
        limit = A[i] / 2
        # limit 以下の最大のインデックスを二分探索で求める
        # bisect_rightはlimitを超える最初の位置を返すので-1してlimit以下の最大インデックスを得る
        pos = bisect.bisect_right(A, limit) - 1
        if pos >= 0:
            total += pos + 1  # 0-basedなので個数はpos+1

    print(total)

if __name__ == "__main__":
    main()