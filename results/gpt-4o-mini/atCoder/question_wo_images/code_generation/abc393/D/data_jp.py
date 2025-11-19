def min_operations_to_group_ones(N, S):
    first_one = S.find('1')
    last_one = S.rfind('1')
    
    return S[first_one:last_one + 1].count('0')

N = int(input().strip())
S = input().strip()
print(min_operations_to_group_ones(N, S))