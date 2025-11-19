#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long power(long long a, long long b) {
 long long res = 1;
 while (b > 0) {
 if (b & 1) res = res * a % MOD;
 a = a * a % MOD;
 b >>= 1;
 }
 return res;
}

bool isPrime(int n) {
 if (n <= 1) return false;
 if (n == 2) return true;
 if (n % 2 == 0) return false;
 for (int i = 3; i * i <= n; i += 2) {
 if (n % i == 0) return false;
 }
 return true;
}

int main() {
 ios_base::sync_with_stdio(false);
 cin.tie(0);

 int N;
 cin >> N;

 long long ans = power(N, N - 2); 

 for (int k = 2; k <= N; k++) {
 if (isPrime(k)) {
 long long count = 1;
 for (int i = 0; i < k; i++) {
 count = count * (N - i) % MOD;
 }
 count = count * power(k, MOD - 2) % MOD;
 ans = (ans + count) % MOD;
 }
 }

 cout << ans << endl;

 return 0;
}