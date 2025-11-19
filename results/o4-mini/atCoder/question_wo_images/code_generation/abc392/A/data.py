def main():
    A = list(map(int, input().split()))
    
    # Check all combinations of two elements multiplying to the third
    if A[0] * A[1] == A[2] or A[1] * A[2] == A[0] or A[0] * A[2] == A[1]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()