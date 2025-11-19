import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        p = list(map(int, data[index:index + N - 1]))
        index += N - 1
        
        # Step 1: Create a list to store the children of each node
        children = [[] for _ in range(N + 1)]
        for i in range(2, N + 1):
            children[p[i - 2]].append(i)

        # Step 2: Calculate the maximum operations
        total = 0
        
        def dfs(node):
            nonlocal total
            count = 0
            for child in children[node]:
                count += dfs(child)
            if count % 2 == 0:
                total += count // 2
                return 0  # Even count, we can adjust completely
            else:
                total += count // 2
                return 1  # Odd count, one unpaired left

        dfs(1)
        results.append(total)

    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()