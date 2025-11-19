import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

Q = int(input())
divisors = []

for _ in range(Q):
    A, B = map(int, input().split())
    
    # Добавляем новый делитель
    new_divisors = [A]
    
    # Объединяем с существующими делителями, учитывая LCM
    for d in divisors:
        g = gcd(d, A)
        if g > 1:
            # Есть общие делители, нужно учесть включение-исключение
            new_divisors.append(d)
        else:
            new_divisors.append(d)
    
    # Упрощаем список делителей
    divisors = []
    for d in new_divisors:
        add = True
        for existing in divisors:
            if d % existing == 0:
                add = False
                break
        if add:
            divisors = [existing for existing in divisors if existing % d != 0]
            divisors.append(d)
    
    # Ищем B-й элемент, не делящийся ни на один из делителей
    count = 0
    num = 1
    
    while count < B:
        is_valid = True
        for d in divisors:
            if num % d == 0:
                is_valid = False
                break
        
        if is_valid:
            count += 1
            if count == B:
                print(num)
                break
        
        num += 1