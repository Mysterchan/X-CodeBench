def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, D = map(int, data[0].split())
    snakes = [tuple(map(int, line.split())) for line in data[1:N+1]]
    
    for k in range(1, D + 1):
        max_weight = max(T * (L + k) for T, L in snakes)
        print(max_weight)

if __name__ == "__main__":
    main()