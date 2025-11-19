A = list(map(int, input().split()))

# Проверяем все возможные перестановки
for i in range(3):
    for j in range(3):
        if i != j:
            k = 3 - i - j  # Индекс третьего элемента
            if A[i] * A[j] == A[k]:
                print("Yes")
                exit()

print("No")