def solve():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # Если суммы не равны, невозможно
    if sum(A) != sum(B):
        print("No")
        return
    
    # Если последовательности уже равны
    if A == B:
        print("Yes")
        return
    
    # Создаем канонические представления
    def get_canonical(seq):
        # Найдем все позиции единиц
        ones = [i for i, val in enumerate(seq) if val == 1]
        
        if len(ones) == 0:
            return tuple()
        
        # Вычислим разности между последовательными позициями единиц
        gaps = []
        for i in range(1, len(ones)):
            gaps.append(ones[i] - ones[i-1])
        
        # Добавим циклическую разность
        if len(ones) > 1:
            gaps.append(len(seq) - ones[-1] + ones[0])
        
        # Канонический вид - минимальная ротация
        if len(gaps) == 0:
            return tuple()
        
        min_rotation = gaps[:]
        for i in range(1, len(gaps)):
            rotation = gaps[i:] + gaps[:i]
            if rotation < min_rotation:
                min_rotation = rotation
        
        return tuple(min_rotation)
    
    # Если только 0 или 1 единица, операции не меняют последовательность
    if sum(A) <= 1:
        print("Yes" if A == B else "No")
        return
    
    canon_A = get_canonical(A)
    canon_B = get_canonical(B)
    
    print("Yes" if canon_A == canon_B else "No")

T = int(input())
for _ in range(T):
    solve()