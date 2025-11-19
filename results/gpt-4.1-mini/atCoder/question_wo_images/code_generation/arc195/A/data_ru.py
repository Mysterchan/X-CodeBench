import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Найдем для каждого i в B минимальный индекс в A, где можно найти B[i] после позиции для B[i-1]
pos = [-1] * M
idx = 0
for i in range(N):
    if idx < M and A[i] == B[idx]:
        pos[idx] = i
        idx += 1
if idx < M:
    # B не является подпоследовательностью A ни разу
    print("No")
    exit()

# Аналогично найдем с конца: для каждого i в B максимальный индекс в A, где можно найти B[i] перед позицией для B[i+1]
pos_r = [-1] * M
idx = M - 1
for i in range(N - 1, -1, -1):
    if idx >= 0 and A[i] == B[idx]:
        pos_r[idx] = i
        idx -= 1
if idx >= 0:
    # B не является подпоследовательностью A ни разу (на всякий случай)
    print("No")
    exit()

# Если существует хотя бы две подпоследовательности B в A, то существует i (0 <= i < M-1),
# для которого pos[i] < pos_r[i+1].
# Это означает, что можно выбрать разные индексы для B[i] и B[i+1], что даст разные подпоследовательности.
for i in range(M - 1):
    if pos[i] < pos_r[i + 1]:
        print("Yes")
        break
else:
    # Если такого i нет, то проверим, есть ли хотя бы два варианта для первого или последнего элемента B
    # Проверим, сколько раз B[0] встречается в A до pos[0]
    count_first = 0
    for i in range(pos[0] + 1):
        if A[i] == B[0]:
            count_first += 1
            if count_first >= 2:
                print("Yes")
                break
    else:
        # Проверим, сколько раз B[M-1] встречается в A после pos_r[M-1]
        count_last = 0
        for i in range(pos_r[M - 1], N):
            if A[i] == B[M - 1]:
                count_last += 1
                if count_last >= 2:
                    print("Yes")
                    break
        else:
            print("No")