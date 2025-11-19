def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    P = list(map(int, data[1:N+1]))
    Q = list(map(int, data[N+1:2*N+1]))
    
    # Create a mapping from person index to their number
    number_by_person = [0] * (N + 1)
    for i in range(1, N + 1):
        number_by_person[i] = Q[i - 1]
    
    # Prepare the result array
    result = [0] * N
    
    for i in range(1, N + 1):
        # Person i is looking at person P[i-1]
        person_looked_at = P[i - 1]
        # Get the number on the looked-at person's jersey
        result[i - 1] = number_by_person[person_looked_at]
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()