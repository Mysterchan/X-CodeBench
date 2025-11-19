def main():
    N = int(input())
    for r in range(1, N+1):
        row = []
        for c in range(1, N+1):
            # distance to the nearest border
            d = min(r, c, N+1-r, N+1-c)
            # odd layers are black ('#'), even are white ('.')
            row.append('#' if d % 2 == 1 else '.')
        print("".join(row))

if __name__ == "__main__":
    main()