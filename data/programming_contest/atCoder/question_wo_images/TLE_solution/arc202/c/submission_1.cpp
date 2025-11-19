#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>

using u32 = uint32_t;

constexpr u32 mod = 998'244'353;

u32 add(u32 a, u32 b, u32 md = mod) {
    return a + b - md * (a + b >= md);
}
void add_to(u32& a, u32 b, u32 md = mod) {
    a = add(a, b, md);
}
u32 mul(u32 a, u32 b) {
    return a * uint64_t(b) % mod;
}
void mul_by(u32& a, u32 b) {
    a = mul(a, b);
}
u32 power(u32 b, u32 e) {
    u32 r = 1;
    for (; e; e >>= 1) {
        if (e & 1)
            r = mul(r, b);
        b = mul(b, b);
    }
    return r;
}

int32_t main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> input(n);
    for (auto& i : input) {
        std::cin >> i;
    }

    int m = *std::max_element(input.begin(), input.end()) + 1;

    std::vector<std::vector<int>> divs(m);
    for (int i = 1; i < m; i++) {
        for (int j = i; j < m; j += i) {
            divs[j].push_back(i);
        }
    }
    std::vector<int> primes;
    std::vector<std::vector<int>> pdivs(m);
    for (int i = 1; i < m; i++) {
        if (divs[i].size() == 2) {
            primes.push_back(i);
            for (int j = i; j < m; j += i) {
                pdivs[j].push_back(i);
            }
        }
    }
    std::vector<int> mu(m);
    mu[1] = 1;
    for (int i = 2; i < m; i++) {
        int cnt = 0;
        int p = divs[i][1];
        int j = i;
        do {
            j /= p, cnt++;
        } while (j % p == 0);
        mu[i] = -1 * mu[i / p] * (cnt == 1);
    }

    std::vector<u32> dp(m, 0);
    std::vector<u32> dp2(m, 0);
    u32 ans = 1;

    for (int val : input) {
        for (int d : divs[val]) {
            u32 dlt = 0;
            for (int q : divs[val / d]) {
                if (mu[q] == 1) {
                    add_to(dlt, dp2[d * q], mod - 1);
                } else if (mu[q] == -1) {
                    add_to(dlt, (mod - 1) - dp2[d * q], mod - 1);
                }
            }
            if (d == val) {
                add_to(dlt, (mod - 1) - 1, mod - 1);
            }
            dlt = add(0, (mod - 1) - dlt, mod - 1);
            add_to(dp[d], dlt, mod - 1);

            u32 f = add(power(10, d), mod - 1);
            mul_by(ans, power(f, dlt));

            for (int d2 : divs[d]) {
                add_to(dp2[d2], dlt, mod - 1);
            }
        }

        std::cout << mul(ans, power(9, mod - 2)) << "\n";
    }

    return 0;
}
