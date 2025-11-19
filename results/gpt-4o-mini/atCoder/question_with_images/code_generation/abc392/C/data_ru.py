def find_numbers_on_chests(N, P, Q):
    # Создаем словарь для сопоставления нагрудников с их индексами
    index_by_chest_number = {Q[i]: i + 1 for i in range(N)}
    
    # Создаем список для хранения результатов
    result = [0] * N
    
    # Для каждого человека находим номер нагрудника, на который он смотрит
    for i in range(N):
        person_index = P[i] - 1  # Индекс человека, который смотрит
        looked_at_person_index = index_by_chest_number[Q[person_index]]  # Индекс человека, на которого он смотрит
        result[i] = Q[looked_at_person_index - 1]  # Номер нагрудника на человеке, на которого он смотрит
    
    return result

# Чтение входных данных
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
P = list(map(int, data[1:N+1]))
Q = list(map(int, data[N+1:2*N+1]))

# Получение результата
result = find_numbers_on_chests(N, P, Q)

# Вывод результата
print(" ".join(map(str, result)))