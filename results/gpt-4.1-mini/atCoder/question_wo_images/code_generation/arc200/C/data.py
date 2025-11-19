def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        people = []
        for i in range(N):
            L, R = map(int, input().split())
            people.append((L, R, i))
        # Sort people by their leaving time R (earliest leave first)
        # If tie, by L ascending, then by index ascending (to ensure lex order)
        people.sort(key=lambda x: (x[1], x[0], x[2]))

        # Assign seats in order 1..N to people sorted by earliest leave time
        # This minimizes dissatisfaction because people who leave earlier get seats closer to left,
        # reducing crossing conflicts.
        # Finally, we need to output P in order of person index (1..N)
        P = [0]*N
        for seat, (_, _, idx) in enumerate(people, start=1):
            P[idx] = seat

        print(*P)

if __name__ == "__main__":
    main()