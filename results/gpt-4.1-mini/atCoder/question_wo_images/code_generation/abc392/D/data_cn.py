import sys
input = sys.stdin.readline

N = int(input())
freqs = []
Ks = []
for _ in range(N):
    data = list(map(int, input().split()))
    K = data[0]
    faces = data[1:]
    Ks.append(K)
    freq = {}
    for f in faces:
        freq[f] = freq.get(f, 0) + 1
    freqs.append(freq)

max_prob = 0.0
for i in range(N):
    Ki = Ks[i]
    fi = freqs[i]
    for j in range(i+1, N):
        Kj = Ks[j]
        fj = freqs[j]
        # Calculate sum of (freq_i[x]/Ki)*(freq_j[x]/Kj) over all x in intersection
        # To optimize, iterate over smaller dict
        if len(fi) < len(fj):
            smaller, bigger = fi, fj
            Ki_, Kj_ = Ki, Kj
        else:
            smaller, bigger = fj, fi
            Ki_, Kj_ = Kj, Ki
        s = 0.0
        for x, cnt in smaller.items():
            if x in bigger:
                s += (cnt / Ki_) * (bigger[x] / Kj_)
        if s > max_prob:
            max_prob = s

print(f"{max_prob:.15f}")