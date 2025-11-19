import sys
input = sys.stdin.read

def solve():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        A = list(map(int, data[index:index + N]))
        index += N
        
        ans = 0
        p = None  # using None for clarity
        # Count the number of transitions between different elements
        for a in A:
            if p is None or p != a:
                ans += 1
            p = a
        
        # Adjust operations based on sequences of same valued elements
        # We can continuously remove pairs of identical adjacent elements in one operation
        for i in range(N - 1):
            if A[i] == A[i + 1]:
                # This means we can count it as part of a reducible sequence
                if i < N - 2 and A[i + 1] == A[i + 2]:
                    ans -= 1  # Further reduce because we can remove three
                    i += 1  # Skip the next one since we already counted it

        results.append(ans)
    
    # Print all results as batch to reduce time on I/O operation
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solve()