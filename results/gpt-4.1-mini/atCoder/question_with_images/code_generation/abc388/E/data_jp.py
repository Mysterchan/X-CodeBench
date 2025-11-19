import sys
import bisect

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))

    left, right = 0, N // 2
    while left < right:
        mid = (left + right + 1) // 2
        # A[mid:] の最小値は A[mid]
        # A[:mid] の最大値は A[mid-1]
        # それぞれの i について A[i] * 2 <= A[mid + i] が成り立つか確認
        # つまり、A[i] <= A[mid + i] / 2
        # mid 個のペアを作れるか判定
        ok = True
        for i in range(mid):
            if A[i] * 2 > A[mid + i]:
                ok = False
                break
        if ok:
            left = mid
        else:
            right = mid - 1

    print(left)

if __name__ == "__main__":
    main()