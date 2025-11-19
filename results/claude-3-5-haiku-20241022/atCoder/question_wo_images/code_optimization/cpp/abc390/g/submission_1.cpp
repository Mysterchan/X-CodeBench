#include <bits/stdc++.h>

using namespace std;

const int Mod = 998244353;

int binPow(long long x, int y){
    int res = 1;
    x %= Mod;
    for (; y > 0; x = x * x % Mod, y >>= 1){
        if (y & 1) res = res * x % Mod;
    }
    return res;
}

void DFT(vector<int> &c, bool inv = false){
    int n = c.size(), lg = __builtin_ctz(n);
    
    for (int i = 0; i < n; i++){
        int j = 0;
        for (int k = 0; k < lg; k++){
            if (i >> k & 1) j |= 1 << (lg - k - 1);
        }
        if (i < j) swap(c[i], c[j]);
    }
    
    for (int b = 1; b <= lg; b++){
        int k = 1 << b, w = binPow(3, (Mod - 1) / k);
        if (inv) w = binPow(w, Mod - 2);
        
        for (int i = 0; i < n; i += k){
            int pw = 1;
            for (int j = i; j < i + k / 2; j++){
                int u = c[j], v = (long long)c[j + k / 2] * pw % Mod;
                c[j] = (u + v) % Mod;
                c[j + k / 2] = (u - v + Mod) % Mod;
                pw = (long long)pw * w % Mod;
            }
        }
    }
    
    if (inv){
        int invn = binPow(n, Mod - 2);
        for (auto &x: c) x = (long long)x * invn % Mod;
    }
}

vector<int> convolution(vector<int> A, vector<int> B){
    int sz = A.size() + B.size() - 1;
    int n = 1;
    while (n < sz) n <<= 1;
    
    A.resize(n), B.resize(n);
    DFT(A), DFT(B);
    
    for (int i = 0; i < n; i++) A[i] = (long long)A[i] * B[i] % Mod;
    
    DFT(A, true);
    A.resize(sz);
    return A;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    if (n == 1){
        cout << "1\n";
        return 0;
    }
    
    vector<int> fact(n + 1);
    fact[0] = 1;
    for (int i = 1; i <= n; i++){
        fact[i] = (long long)fact[i - 1] * i % Mod;
    }
    
    vector<int> digits(n + 1), pw10(6);
    pw10[0] = 1;
    for (int i = 1; i < 6; i++) pw10[i] = pw10[i - 1] * 10;
    
    for (int i = 1; i <= n; i++){
        digits[i] = to_string(i).size();
    }
    
    vector<int> sum(6);
    
    for (int d = 1; d <= 5 && pw10[d - 1] <= n; d++){
        vector<int> A = {1};
        
        for (int x = 1; x <= n; x++){
            if (digits[x] != d){
                A = convolution(A, {1, pw10[digits[x]]});
            }
        }
        
        for (int k = 0; k < n; k++){
            if (k < (int)A.size()){
                sum[d - 1] = (sum[d - 1] + (long long)A[k] * fact[k] % Mod * fact[n - k - 1]) % Mod;
            }
        }
    }
    
    int ans = 0;
    for (int x = 1; x <= n; x++){
        ans = (ans + (long long)sum[digits[x] - 1] * x) % Mod;
    }
    
    cout << ans << '\n';
    
    return 0;
}