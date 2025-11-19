def count_permutations(t, cases):
    MOD = 998244353
    results = []

    for n, s in cases:
        possible_positions = [[] for _ in range(n)]
        fixed_scores = {}
        
        for i in range(n):
            if s[i] != -1:
                fixed_scores[i] = s[i]
            else:
                for j in range(n):
                    possible_positions[j].append(i)

        # To keep count of possible placements
        def is_possible():
            for idx, score in fixed_scores.items():
                black_cells = 0
                # Check left
                for i in range(idx - 1, -1, -1):
                    if i not in fixed_scores:
                        continue
                    if s[i] == -1:  
                        black_cells += 1
                    else:
                        break
                # Check right
                for i in range(idx + 1, n):
                    if i not in fixed_scores:
                        continue
                    if s[i] == -1:
                        black_cells += 1
                    else:
                        break
                if black_cells < score:
                    return False
            return True

        def backtrack(selected, used):
            if len(selected) == n:
                return 1

            total_count = 0
            for i in range(n):
                if not used[i] and i in possible_positions[len(selected)]:
                    selected.append(i)
                    used[i] = True
                    if is_possible():
                        total_count += backtrack(selected, used)
                    selected.pop()
                    used[i] = False

            return total_count % MOD

        used = [False] * n
        total_permutations = backtrack([], used)
        results.append(total_permutations)

    return results


# Input processing
t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    cases.append((n, s))

results = count_permutations(t, cases)
print('\n'.join(map(str, results)))