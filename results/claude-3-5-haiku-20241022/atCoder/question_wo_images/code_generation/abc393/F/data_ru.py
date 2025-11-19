import bisect

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    
    for _ in range(Q):
        R, X = map(int, input().split())
        
        # Найти длину самой длинной строго возрастающей подпоследовательности
        # из первых R элементов, где все элементы <= X
        lis = []
        
        for i in range(R):
            if A[i] <= X:
                pos = bisect.bisect_left(lis, A[i])
                if pos < len(lis):
                    lis[pos] = A[i]
                else:
                    lis.append(A[i])
        
        print(len(lis))

solve()