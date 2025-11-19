import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

left, right = 0, N // 2
res = 0

while left <= right:
    mid = (left + right) // 2
    # Проверяем, можно ли сформировать mid пар
    # Берём mid самых маленьких и mid самых больших элементов
    # Проверяем условие a_i <= b_j / 2 для каждой пары
    possible = True
    for i in range(mid):
        if A[i] * 2 > A[N - mid + i]:
            possible = False
            break
    if possible:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)