import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    S = list(map(int, data[1:n + 1]))
    
    if n < 3:
        print(0)
        return

    S_set = set(S)
    count = 0

    for B in S:
        A = B - 1
        C = B + 1
        while A > 0 and C <= 1000000:
            if A in S_set and C in S_set:
                count += 1
            A -= 1
            C += 1

    print(count)

if __name__ == '__main__':
    main()