import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [0] + list(map(int, input().split()))
    
    # extra[i] will be the difference-array for how many gifts start giving
    # at year i.  We only need up to N+1.
    extra = [0] * (N + 2)
    
    D = [0] * (N + 1)  # D[i] = stones immediately after alien i becomes adult
    C = 0              # running prefix sum for gifts arriving at year i
    
    for i in range(1, N + 1):
        # incorporate any new contributions that start at year i
        C += extra[i]
        
        # total stones alien i has the moment it becomes adult
        D[i] = A[i] + C
        
        # this alien will give 1 stone to each new adult at years i+1,...,i+D[i]
        l = i + 1
        r = min(N, i + D[i])
        if l <= r:
            extra[l]   += 1
            extra[r+1] -= 1
    
    # Finally, after year N each alien i has given away min(D[i], N-i) stones
    # so what's left is max(0, D[i] - (N-i)).
    ans = [str(max(0, D[i] - (N - i))) for i in range(1, N + 1)]
    print(" ".join(ans))

if __name__ == "__main__":
    main()