A = list(map(int, input().split()))

# Проверяем, можно ли отсортировать массив ровно одним обменом смежных элементов
sorted_A = [1, 2, 3, 4, 5]

# Если массив уже отсортирован, нужно выполнить операцию, но это не поможет
if A == sorted_A:
    print("No")
else:
    # Пробуем все возможные обмены смежных элементов
    found = False
    for i in range(4):  # Индексы от 0 до 3 (обмен i и i+1)
        # Создаем копию и меняем местами смежные элементы
        temp = A.copy()
        temp[i], temp[i+1] = temp[i+1], temp[i]
        
        # Проверяем, стал ли массив отсортированным
        if temp == sorted_A:
            found = True
            break
    
    if found:
        print("Yes")
    else:
        print("No")