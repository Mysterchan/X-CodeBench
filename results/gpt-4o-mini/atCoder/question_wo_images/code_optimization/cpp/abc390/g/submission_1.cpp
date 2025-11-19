#include <bits/stdc++.h>

using namespace std;

const int Mod = 998244353;

void add(int &x, const int &y){
	x += y; 
	if (x >= Mod) x -= Mod; 
}

int main() {
	int n; cin >> n;
	
	// Precompute powers of 10 mod Mod and factorials mod Mod
	vector<long long> pow10(n + 1, 1);
	vector<long long> fact(n + 1, 1);
	for (int i = 1; i <= n; ++i) {
		fact[i] = fact[i - 1] * i % Mod;
		pow10[i] = pow10[i - 1] * 10 % Mod;
	}

	long long ans = 0;
	long long totalPermutations = fact[n];  // This is n! 
	long long mult = 0;

	// Compute the contribution of each position in the permutations
	for (int pos = 1; pos <= n; pos++) {
		int count = (n - pos + 1) * fact[n - 1] % Mod; // How many times this position is filled
		mult = (mult + count * pow10[pos] % Mod) % Mod; // Multiply by position contribution
	} 

	ans = totalPermutations * mult % Mod; // Total permutations times multiplier
	cout << ans << '\n';

	return 0;
}