def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Используем set для хранения уникальных последовательностей
    sequences = set()
    
    # Перебираем все возможные пары (L, R)
    for l in range(n):
        for r in range(l, n):
            # Создаем новую последовательность после операции
            new_seq = a[:l] + [a[l]] * (r - l + 1) + a[r+1:]
            sequences.add(tuple(new_seq))
    
    print(len(sequences))

solve()