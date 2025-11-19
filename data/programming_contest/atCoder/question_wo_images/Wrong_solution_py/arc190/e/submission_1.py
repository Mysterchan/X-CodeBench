def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    pref_sum = [0] * (n + 1)
    for i in range(n):
        pref_sum[i + 1] = pref_sum[i] + a[i]

    pref_odd = [0] * (n + 1)
    pref_even = [0] * (n + 1)
    for i in range(n):
        if i % 2 == 0:
            pref_even[i + 1] = pref_even[i] + a[i]
            pref_odd[i + 1] = pref_odd[i]
        else:
            pref_odd[i + 1] = pref_odd[i] + a[i]
            pref_even[i + 1] = pref_even[i]

    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        total = pref_sum[r + 1] - pref_sum[l]
        odd = pref_odd[r + 1] - pref_odd[l]
        even = pref_even[r + 1] - pref_even[l]

        if (r - l + 1) % 2 == 1:
            if r % 2 == 1:
                odd -= a[r]
            else:
                even -= a[r]
            print(min(odd, even) + (total - min(odd, even) * 2) // 3)
        else:
            print(min(odd, even) + (total - min(odd, even) * 2) // 3)

if __name__ == "__main__":
    main()