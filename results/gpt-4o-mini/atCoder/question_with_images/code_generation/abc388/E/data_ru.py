def max_kadimo(N, A):
    left, right = 0, N - 1
    pairs = 0
    
    while left < right:
        if A[left] * 2 <= A[right]:
            pairs += 1
            left += 1
            right -= 1
        else:
            left += 1

    return pairs

# Ввод данных
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Вывод результата
print(max_kadimo(N, A))