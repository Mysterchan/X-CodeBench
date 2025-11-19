N = int(input())
S = [int(a) for a in input()]
P = 998244353

# X[k] represents the count for each bitmask state k
# Bit 0: used (first edge direction chosen)
# Bit 1: used_first (direction of first edge)
# Bit 2: nused (current edge direction)
# Bit 3: nused_first (for next iteration)

X = [0] * 16
X[9] = 1  # Initial state: bits 0 and 3 set (binary 1001)

for i in range(N):
    nX = [0] * 16
    s_val = S[i]
    is_last = (i == N - 1)
    
    for k in range(16):
        if X[k] == 0:
            continue
        
        x_val = X[k]
        
        # Extract bits from k
        for used_bit in range(2):
            if not (k >> used_bit) & 1:
                continue
                
            for used_first_bit in range(2):
                if not (k >> (used_bit * 2 + used_first_bit)) & 1:
                    continue
                
                nused_first = used_first_bit
                
                for nused in range(2):
                    # Check constraint for last iteration
                    if is_last and nused != used_first_bit:
                        continue
                    
                    # Calculate contributions for each 'a' value
                    for a in range(s_val + 1):
                        nval = (1 - used_bit) + nused + a
                        nk = (1 << (nused * 2 + nused_first))
                        nX[nk] = (nX[nk] + x_val) % P
    
    X = nX

# Sum all non-zero states
result = 0
for k in range(1, 16):
    result = (result + X[k]) % P

print(result)