N, Q = map(int, input().split())

# pigeon_location[i] хранит текущее гнездо голубя i
pigeon_location = [0] + list(range(1, N + 1))  # pigeon_location[i] = i изначально

# nest_count[i] хранит количество голубей в гнезде i
nest_count = [0] * (N + 1)
for i in range(1, N + 1):
    nest_count[i] = 1

# Счетчик гнезд с более чем одним голубем
nests_with_multiple = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        P, H = query[1], query[2]
        
        # Текущее гнездо голубя P
        current_nest = pigeon_location[P]
        
        # Уменьшаем количество в текущем гнезде
        if nest_count[current_nest] == 2:
            nests_with_multiple -= 1
        nest_count[current_nest] -= 1
        
        # Увеличиваем количество в новом гнезде
        if nest_count[H] == 1:
            nests_with_multiple += 1
        nest_count[H] += 1
        
        # Обновляем местоположение голубя
        pigeon_location[P] = H
    
    else:  # query[0] == 2
        print(nests_with_multiple)