import sys
input = sys.stdin.read

def can_transform(T, cases):
    results = []
    for case in cases:
        N, A, B = case
        if A.count(1) == B.count(1) and A.count(0) == B.count(0):
            results.append("Yes")
        else:
            results.append("No")
    return results

def main():
    data = input().splitlines()
    T = int(data[0])
    cases = []
    index = 1
    for _ in range(T):
        N = int(data[index])
        A = list(map(int, data[index + 1].split()))
        B = list(map(int, data[index + 2].split()))
        cases.append((N, A, B))
        index += 3
    results = can_transform(T, cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()