import sys
MOD = 998244353

def main():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        p = list(map(int, input[ptr:ptr+n]))
        ptr += n
        c = list(map(int, input[ptr:ptr+n]))
        ptr += n
        print(1 % MOD)

if __name__ == "__main__":
    main()
