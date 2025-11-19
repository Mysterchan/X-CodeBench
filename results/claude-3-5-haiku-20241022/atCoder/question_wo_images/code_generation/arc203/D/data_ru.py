def solve():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    
    def min_length(arr):
        # Найти минимальную длину B, из которой можно получить arr
        # Ключевое наблюдение: мы можем "сжимать" последовательность
        # удаляя соседние элементы, если между ними можно вставить их XOR
        
        # Если у нас есть подпоследовательность вида x, y, z, ...
        # и мы хотим получить ее из более короткой последовательности,
        # мы можем удалить средние элементы, если они являются XOR соседних
        
        # Минимальная длина достигается, когда мы максимально сжимаем
        # последовательность, удаляя все элементы, которые являются XOR соседних
        
        if len(arr) == 0:
            return 0
        
        # Подход: используем динамическое программирование или жадный алгоритм
        # Ключевая идея: если arr[i] == arr[i-1] XOR arr[i+1], то arr[i] можно удалить
        
        # Попробуем рекурсивно уменьшать массив
        while True:
            changed = False
            new_arr = [arr[0]]
            
            for i in range(1, len(arr) - 1):
                # Проверяем, можно ли удалить arr[i]
                if arr[i] == (new_arr[-1] ^ arr[i + 1]):
                    # Можем удалить этот элемент
                    changed = True
                else:
                    new_arr.append(arr[i])
            
            if len(arr) > 0:
                new_arr.append(arr[-1])
            
            arr = new_arr
            
            if not changed or len(arr) <= 2:
                break
        
        return len(arr)
    
    for _ in range(q):
        i = int(input())
        a[i - 1] = 1 - a[i - 1]
        print(min_length(a))

solve()