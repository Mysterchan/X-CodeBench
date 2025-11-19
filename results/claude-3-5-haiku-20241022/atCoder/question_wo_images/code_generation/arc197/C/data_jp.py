def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

Q = int(input())
removed = []

for _ in range(Q):
    A, B = map(int, input().split())
    
    # Add A to the list of removed multipliers
    new_removed = [A]
    for r in removed:
        g = gcd(A, r)
        if g < A:
            new_removed.append(A // g)
    removed.extend(new_removed)
    
    # Find B-th smallest number not divisible by any removed multiplier
    count = 0
    num = 1
    while count < B:
        is_valid = True
        for r in removed:
            if num % r == 0:
                is_valid = False
                break
        if is_valid:
            count += 1
            if count == B:
                print(num)
                break
        num += 1