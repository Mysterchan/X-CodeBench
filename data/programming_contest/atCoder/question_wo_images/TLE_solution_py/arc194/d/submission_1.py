from collections import deque

MOD = 998244353

def count_distinct_sequences(N, S):
    queue = deque([S])
    seen = set([S])

    while queue:
        current = queue.popleft()

        for l in range(N):
            for r in range(l, N):
                substring = current[l:r+1]

                if is_valid(substring):

                    reversed_substring = substring[::-1].translate(str.maketrans("()", ")("))
                    new_seq = current[:l] + reversed_substring + current[r+1:]

                    if new_seq not in seen:
                        seen.add(new_seq)
                        queue.append(new_seq)

    return len(seen) % MOD

def is_valid(seq):
    balance = 0
    for char in seq:
        balance += 1 if char == '(' else -1
        if balance < 0:
            return False
    return balance == 0

N = int(input().strip())
S = input().strip()

print(count_distinct_sequences(N, S))