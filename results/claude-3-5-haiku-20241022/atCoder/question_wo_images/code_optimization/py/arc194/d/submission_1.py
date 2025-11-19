MOD = 998244353

def count_distinct_sequences(N, S):
    # Precompute all valid substrings
    valid = [[False] * N for _ in range(N)]
    
    for length in range(2, N + 1, 2):
        for l in range(N - length + 1):
            r = l + length - 1
            balance = 0
            is_valid_seq = True
            for i in range(l, r + 1):
                balance += 1 if S[i] == '(' else -1
                if balance < 0:
                    is_valid_seq = False
                    break
            if is_valid_seq and balance == 0:
                valid[l][r] = True
    
    # BFS with optimized string handling
    queue = [S]
    seen = {S}
    head = 0
    
    while head < len(queue):
        current = queue[head]
        head += 1
        
        for l in range(N):
            for r in range(l + 1, N, 2):
                if not valid[l][r]:
                    continue
                
                # Build new sequence directly
                new_seq_parts = []
                if l > 0:
                    new_seq_parts.append(current[:l])
                
                # Reverse and swap parentheses
                for i in range(r, l - 1, -1):
                    new_seq_parts.append(')' if current[i] == '(' else '(')
                
                if r + 1 < N:
                    new_seq_parts.append(current[r + 1:])
                
                new_seq = ''.join(new_seq_parts)
                
                if new_seq not in seen:
                    seen.add(new_seq)
                    queue.append(new_seq)
    
    return len(seen) % MOD

N = int(input().strip())
S = input().strip()

print(count_distinct_sequences(N, S))