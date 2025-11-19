import sys
input = sys.stdin.readline

N = int(input())
freqs = []
Ks = []
Amax = 0

for _ in range(N):
    data = list(map(int, input().split()))
    K = data[0]
    faces = data[1:]
    Ks.append(K)
    freq = {}
    for f in faces:
        freq[f] = freq.get(f, 0) + 1
        if f > Amax:
            Amax = f
    freqs.append(freq)

# Precompute frequency arrays for faster access
# Convert dicts to arrays for O(1) access
freq_arrays = [ [0]*(Amax+1) for _ in range(N) ]
for i in range(N):
    for val, count in freqs[i].items():
        freq_arrays[i][val] = count

res = 0.0
for i in range(N):
    Ki = Ks[i]
    fi = freq_arrays[i]
    for j in range(i+1, N):
        Kj = Ks[j]
        fj = freq_arrays[j]
        # sum of freq[i][x]*freq[j][x] over x
        s = 0
        fi_j = fi
        fj_j = fj
        # Since Amax can be up to 10^5, iterate over all
        # but to optimize, iterate over smaller freq dict keys
        # Instead of iterating all Amax+1, iterate over keys of smaller freq dict
        # To do this, find which freq dict has fewer non-zero entries
        # We'll do this by checking counts of non-zero entries
        # But to avoid overhead, just iterate over keys of freq dict with fewer keys

        # Let's do this optimization:
        # Count non-zero entries for i and j
        # We'll store non-zero keys for each freq dict once
        pass

# To optimize further, precompute non-zero keys for each freq dict
nonzero_keys = []
for i in range(N):
    keys = [k for k,v in freqs[i].items()]
    nonzero_keys.append(keys)

res = 0.0
for i in range(N):
    Ki = Ks[i]
    fi = freq_arrays[i]
    keys_i = nonzero_keys[i]
    for j in range(i+1, N):
        Kj = Ks[j]
        fj = freq_arrays[j]
        keys_j = nonzero_keys[j]
        # Iterate over smaller keys list
        if len(keys_i) < len(keys_j):
            s = 0
            for k in keys_i:
                s += fi[k]*fj[k]
        else:
            s = 0
            for k in keys_j:
                s += fi[k]*fj[k]
        val = s/(Ki*Kj)
        if val > res:
            res = val

print(res)