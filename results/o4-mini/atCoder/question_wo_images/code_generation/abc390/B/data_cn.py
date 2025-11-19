import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    # 长度为2的序列总是几何级数
    if n <= 2:
        print("Yes")
        return

    # 对每个位置i（从1到n-2），检查A[i]^2 == A[i-1] * A[i+1]
    for i in range(1, n-1):
        if A[i] * A[i] != A[i-1] * A[i+1]:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()