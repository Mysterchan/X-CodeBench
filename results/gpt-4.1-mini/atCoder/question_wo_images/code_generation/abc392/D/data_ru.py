import sys
import math

def main():
    input = sys.stdin.readline
    N = int(input())
    dice = []
    for _ in range(N):
        data = list(map(int, input().split()))
        K = data[0]
        faces = data[1:]
        freq = {}
        for f in faces:
            freq[f] = freq.get(f, 0) + 1
        dice.append((K, freq))

    max_prob = 0.0
    for i in range(N):
        K_i, freq_i = dice[i]
        for j in range(i+1, N):
            K_j, freq_j = dice[j]
            # To optimize, iterate over smaller freq dict
            if len(freq_i) < len(freq_j):
                smaller, larger = freq_i, freq_j
            else:
                smaller, larger = freq_j, freq_i
            prob = 0.0
            for val, count_i in smaller.items():
                count_j = larger.get(val)
                if count_j is not None:
                    prob += (count_i / K_i) * (count_j / K_j)
            if prob > max_prob:
                max_prob = prob

    print(f"{max_prob:.15f}")

if __name__ == "__main__":
    main()