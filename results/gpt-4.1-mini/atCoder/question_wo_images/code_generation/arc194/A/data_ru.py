import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
current_sum = 0

for x in A:
    if not stack:
        # S пуст, нужно добавить элемент
        stack.append(x)
        current_sum += x
    else:
        if x >= 0:
            # Добавляем положительный элемент
            stack.append(x)
            current_sum += x
        else:
            # Отрицательный элемент
            # Решаем: добавить или удалить последний элемент
            # Если удаление выгоднее (удаляем элемент с меньшим значением, чем x),
            # то удаляем, иначе добавляем x
            if stack[-1] < x:
                # Удаляем последний элемент
                removed = stack.pop()
                current_sum -= removed
            else:
                # Добавляем отрицательный элемент
                stack.append(x)
                current_sum += x

print(current_sum)