import sys
import bisect

def main():
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    
    count = 0
    for i in range(N):
        # Для A[i] ищем количество A[j], таких что A[j] >= 2 * A[i]
        # j > i, т.к. кагаэмичи - два мооти, одно на другом, порядок важен
        # Используем бинарный поиск для поиска левого индекса j
        target = 2 * A[i]
        j = bisect.bisect_left(A, target, i+1, N)
        count += N - j
    
    print(count)

if __name__ == "__main__":
    main()