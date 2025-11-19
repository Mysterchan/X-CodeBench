def main():
    A = list(map(int, input().split()))
    target = [1, 2, 3, 4, 5]
    for i in range(4):
        A[i], A[i+1] = A[i+1], A[i]
        if A == target:
            print("Yes")
            return
        A[i], A[i+1] = A[i+1], A[i]
    print("No")

if __name__ == "__main__":
    main()