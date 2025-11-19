import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
    
    n = int(data[0])
    S = list(map(int, data[1:1 + n]))
    
    if n < 3:
        print(0)
        return
    
    S_set = set(S)
    S.sort()
    
    total_count = 0
    
    for i in range(n):
        B = S[i]
        # For each B, count pairs (A, C) where A < B < C and A + C = 2B
        for j in range(i):
            A = S[j]  # A < B guaranteed by sorted order
            C = 2 * B - A
            if C > B and C in S_set:
                total_count += 1
    
    print(total_count)

if __name__ == '__main__':
    main()