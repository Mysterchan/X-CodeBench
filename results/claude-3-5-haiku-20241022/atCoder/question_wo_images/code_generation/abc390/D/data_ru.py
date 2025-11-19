def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    xor_values = set()
    
    # Генерируем все разбиения множества {0, 1, ..., n-1}
    # Используем представление через функцию: каждый элемент принадлежит группе с номером
    def generate_partitions(n):
        # Для каждого элемента храним номер его группы
        def backtrack(idx, partition, max_group):
            if idx == n:
                yield [group[:] for group in partition]
                return
            
            # Добавляем элемент idx в существующую группу
            for i in range(max_group + 1):
                partition[i].append(idx)
                yield from backtrack(idx + 1, partition, max(max_group, i))
                partition[i].pop()
            
            # Создаем новую группу для элемента idx
            if max_group + 1 < n:
                partition.append([idx])
                yield from backtrack(idx + 1, partition, max_group + 1)
                partition.pop()
        
        yield from backtrack(0, [[]], -1)
    
    # Для каждого разбиения вычисляем XOR
    for partition in generate_partitions(n):
        # Фильтруем пустые группы
        partition = [group for group in partition if group]
        
        xor_result = 0
        for group in partition:
            group_sum = sum(a[i] for i in group)
            xor_result ^= group_sum
        
        xor_values.add(xor_result)
    
    print(len(xor_values))

solve()