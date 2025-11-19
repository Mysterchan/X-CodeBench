def main():
    N, M = map(int, input().split())
    A = set(map(int, input().split()))
    
    missing = [x for x in range(1, N+1) if x not in A]
    
    print(len(missing))
    if missing:
        print(*missing)

if __name__ == "__main__":
    main()