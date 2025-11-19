#include <iostream>
#include <vector>

using u32 = uint32_t;

constexpr u32 mod = 998'244'353;

u32 mul(u32 a, u32 b) {
    return a * uint64_t(b) % mod;
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

u32 lcm(u32 a, u32 b) {
    return a / std::__gcd(a, b) * b % mod;
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

    u32 current_lcm = 1;
    for (int i = 0; i < n; ++i) {
        u32 R = (power(10, input[i]) - 1) / 9;  // Calculate R_{A_i} == (10^A_i - 1) / 9
        current_lcm = lcm(current_lcm, R);
        std::cout << current_lcm << "\n";
    }

    return 0;
}
