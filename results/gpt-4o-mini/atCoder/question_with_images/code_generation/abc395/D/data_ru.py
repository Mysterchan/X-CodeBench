def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, Q = map(int, data[0].split())
    
    # Изначально каждый голубь находится в своем гнезде
    nests = list(range(1, N + 1))
    
    output = []
    
    for i in range(1, Q + 1):
        operation = list(map(int, data[i].split()))
        
        if operation[0] == 1:
            # Тип 1: 1 a b
            a, b = operation[1] - 1, operation[2] - 1
            nests[a] = b + 1  # Перемещаем голубя a в гнездо b
            
        elif operation[0] == 2:
            # Тип 2: 2 a b
            a, b = operation[1] - 1, operation[2] - 1
            # Меняем местами гнезда a и b
            nests[a], nests[b] = nests[b], nests[a]
        
        elif operation[0] == 3:
            # Тип 3: 3 a
            a = operation[1] - 1
            output.append(nests[a])  # Добавляем текущее гнездо голубя a в вывод
    
    # Печатаем все результаты операций типа 3
    sys.stdout.write('\n'.join(map(str, output)) + '\n')

if __name__ == "__main__":
    main()