N, M = map(int, input().split())
S = list(input().strip())
T = input().strip()

for k in range(M):
    char_t = T[k]
    
    # Ищем самую левую позицию, где замена увеличит значение
    best_pos = -1
    for i in range(N):
        if S[i] < char_t:
            best_pos = i
            break
    
    # Если нашли позицию для улучшения, используем её
    # Иначе заменяем последнюю позицию
    if best_pos != -1:
        S[best_pos] = char_t
    else:
        S[N - 1] = char_t

print(''.join(S))