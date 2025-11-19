#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long modPow(long long base, long long exp) {
    long long result = 1;
    while (exp) {
        if (exp % 2) result = result * base % MOD;
        base = base * base % MOD;
        exp /= 2;
    }
    return result;
}

int main() {
    int n;
    string s;
    cin >> n >> s;

    vector<long long> factorial(n + 1, 1), inverse(n + 1);
    for (int i = 1; i <= n; ++i) {
        factorial[i] = factorial[i - 1] * i % MOD;
    }
    inverse[n] = modPow(factorial[n], MOD - 2);
    for (int i = n - 1; i >= 0; --i) {
        inverse[i] = inverse[i + 1] * (i + 1) % MOD;
    }

    stack<int> st;
    vector<long long> count(n + 1, 0);
    vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
    count[0] = 1; // There's one way to form a valid sequence of length 0.

    for (int i = 0; i < n; ++i) {
        if (s[i] == '(') {
            st.push(i);
        } else {
            int l = st.top(); st.pop();
            for (int j = 0; j <= i - l - 1; ++j) {
                count[i + 1] += count[j];
                count[i + 1] %= MOD;
            }
            count[i + 1] *= factorial[i - l + 1]; // The current sequence length with the new pair
            count[i + 1] %= MOD;
        }
    }

    long long result = count[n];
    for (int i = 1; i <= n; ++i) {
        result = result * inverse[i] % MOD; // Divide by the ways to arrange identical brackets
    }

    cout << result << endl;
}
