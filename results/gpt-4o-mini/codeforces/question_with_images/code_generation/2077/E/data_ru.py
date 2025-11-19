def calculate_f(b):
    # находим минимальное количество операций для массива
    max_value = 0
    operations = 0
    for value in b:
        if value > max_value:
            operations += (value - max_value)
            max_value = value
    return operations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    MOD = 998244353
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        total_sum = 0
        
        # Вычисляем сумму по всем подмассивам
        for l in range(n):
            current = []
            for r in range(l, n):
                current.append(a[r])
                total_sum += calculate_f(current)
                total_sum %= MOD
        
        results.append(total_sum)
    
    # Выводим результаты
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()