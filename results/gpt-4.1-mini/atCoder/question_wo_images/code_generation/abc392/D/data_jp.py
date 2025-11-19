import sys
input = sys.stdin.readline

N = int(input())
freqs = []
for _ in range(N):
    data = list(map(int, input().split()))
    K = data[0]
    faces = data[1:]
    freq = {}
    for f in faces:
        freq[f] = freq.get(f, 0) + 1
    # Convert counts to probabilities
    for k in freq:
        freq[k] /= K
    freqs.append(freq)

max_prob = 0.0
for i in range(N):
    fi = freqs[i]
    for j in range(i+1, N):
        fj = freqs[j]
        # Calculate sum of products of probabilities for common faces
        # Iterate over smaller dict for efficiency
        if len(fi) < len(fj):
            smaller, larger = fi, fj
        else:
            smaller, larger = fj, fi
        s = 0.0
        for face, p in smaller.items():
            if face in larger:
                s += p * larger[face]
        if s > max_prob:
            max_prob = s

print(max_prob)