import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        monsters = []
        min_x = float('inf')
        max_x = -float('inf')
        min_y = float('inf')
        max_y = -float('inf')

        x_count = {}
        y_count = {}

        for __ in range(n):
            x, y = map(int, input[ptr:ptr+2])
            ptr +=2
            monsters.append((x, y))
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y

        if min_x == max_x or min_y == max_y:
            print(1)
            continue

        initial_area = (max_x - min_x + 1) * (max_y - min_y + 1)
        min_x_monsters = []
        max_x_monsters = []
        min_y_monsters = []
        max_y_monsters = []

        for x, y in monsters:
            if x == min_x:
                min_x_monsters.append((x, y))
            if x == max_x:
                max_x_monsters.append((x, y))
            if y == min_y:
                min_y_monsters.append((x, y))
            if y == max_y:
                max_y_monsters.append((x, y))

        min_possible = initial_area

        if len(min_x_monsters) == 1:
            second_min_x = float('inf')
            for x, y in monsters:
                if x != min_x and x < second_min_x:
                    second_min_x = x
            if second_min_x != float('inf'):
                new_width = max_x - second_min_x + 1
                new_area = new_width * (max_y - min_y + 1)
                if new_area < min_possible:
                    min_possible = new_area
        if len(max_x_monsters) == 1:
            second_max_x = -float('inf')
            for x, y in monsters:
                if x != max_x and x > second_max_x:
                    second_max_x = x
            if second_max_x != -float('inf'):
                new_width = second_max_x - min_x + 1
                new_area = new_width * (max_y - min_y + 1)
                if new_area < min_possible:
                    min_possible = new_area

        if len(min_y_monsters) == 1:
            second_min_y = float('inf')
            for x, y in monsters:
                if y != min_y and y < second_min_y:
                    second_min_y = y
            if second_min_y != float('inf'):
                new_height = max_y - second_min_y + 1
                new_area = (max_x - min_x + 1) * new_height
                if new_area < min_possible:
                    min_possible = new_area
        if len(max_y_monsters) == 1:
            second_max_y = -float('inf')
            for x, y in monsters:
                if y != max_y and y > second_max_y:
                    second_max_y = y
            if second_max_y != -float('inf'):
                new_height = second_max_y - min_y + 1
                new_area = (max_x - min_x + 1) * new_height
                if new_area < min_possible:
                    min_possible = new_area

        print(min_possible)

solve()
