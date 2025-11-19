N = int(input())
A = list(map(int, input().split()))

# Считаем количество индексов, которые могут быть выбраны
count = sum(1 for a in A if a > 0)

# Если количество индексов четное, выигрывает Снук, иначе Фенек
if count % 2 == 0:
    print("Snuke")
else:
    print("Fennec")