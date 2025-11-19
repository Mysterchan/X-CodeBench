def count_kagaimochi(N, sizes):
    count = 0
    j = 0
    
    # Пройти через все размеры мооти
    for i in range(N):
        # Для текущего размера A[i], найти максимальный размер B[j]
        while j < N and sizes[j] < 2 * sizes[i]:
            j += 1
        # Все размеры B до j подходят
        count += j - i - 1  # исключаем i, потому что A должно быть меньше B

    return count

import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
sizes = list(map(int, data[1:N+1]))

print(count_kagaimochi(N, sizes))