def solve(N, K):
    # Найдем все биты, которые равны 0 в N
    zero_bits = []
    temp = N
    bit_pos = 0
    max_bit = N.bit_length()
    
    for i in range(max_bit):
        if (N >> i) & 1 == 0:
            zero_bits.append(i)
    
    # Количество совместимых чисел определяется нулевыми битами в N
    # Для каждой комбинации нулевых битов мы можем построить число
    num_compatible = 1 << len(zero_bits)
    
    if K > num_compatible:
        return -1
    
    # K-е число строится из (K-1) в двоичном представлении
    # используя позиции нулевых битов
    result = N
    k_minus_1 = K - 1
    
    for i, bit_pos in enumerate(zero_bits):
        if (k_minus_1 >> i) & 1:
            result |= (1 << bit_pos)
    
    return result

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(solve(N, K))