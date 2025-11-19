import sys

def minimal_nodes(L, R):
    count = 0
    current = R
    while current > L:
        temp = current
        k = 0
        while temp % 2 == 0:
            temp //= 2
            k += 1
        while True:
            if current - (1 << k) >= L:
                break
            k -= 1
            if k < 0:
                k = 0
        count += 1
        current -= (1 << k)
    return count

def main():
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    for _ in range(t):
        l1 = int(input[idx])
        r1 = int(input[idx+1])
        l2 = int(input[idx+2])
        r2 = int(input[idx+3])
        idx +=4
        x_count = minimal_nodes(l1, r1)
        y_count = minimal_nodes(l2, r2)
        print(x_count * y_count)

if __name__ == "__main__":
    main()
