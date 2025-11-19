def smoke_in_cell(N, R, C, S):
    # Движения по координатам
    moves = {
        'N': (-1, 0),
        'W': (0, -1),
        'S': (1, 0),
        'E': (0, 1)
    }
    
    # Начальная позиция дыма
    smoke_positions = {(0, 0)}
    result = []

    for t in range(N):
        # Перемещение дыма
        new_positions = set()
        for r, c in smoke_positions:
            dr, dc = moves[S[t]]
            new_positions.add((r + dr, c + dc))
        
        # Если в (0, 0) нет дыма, добавляем новый дым
        if (0, 0) not in smoke_positions:
            new_positions.add((0, 0))
        
        smoke_positions = new_positions
        
        # Проверяем наличие дыма в целевой ячейке (R, C)
        if (R, C) in smoke_positions:
            result.append('1')
        else:
            result.append('0')

    print(''.join(result))

# Чтение входных данных
import sys
input = sys.stdin.read
data = input().splitlines()
N, R, C = map(int, data[0].split())
S = data[1]

smoke_in_cell(N, R, C, S)