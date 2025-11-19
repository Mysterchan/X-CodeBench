import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())

# Сортируем T по убыванию, чтобы использовать самые большие цифры сначала
T.sort(reverse=True)

j = 0  # индекс для T
for i in range(N):
    if j == M:
        break
    # Если текущий символ S меньше, чем текущий символ T, заменяем
    if S[i] < T[j]:
        S[i] = T[j]
        j += 1

print("".join(S))