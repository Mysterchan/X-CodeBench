import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# Создаем словарь: bib_number -> person_index
bib_to_person = [0]*(N+1)
for i in range(N):
    bib_to_person[Q[i]] = i

result = [0]*N
for i in range(1, N+1):
    person = bib_to_person[i]       # человек, у которого нагрудник i
    looked_person = P[person] - 1   # индекс человека, на которого он смотрит
    result[i-1] = Q[looked_person]  # нагрудник того, на кого смотрят

print(*result)