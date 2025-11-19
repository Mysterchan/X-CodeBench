#include <bits/stdc++.h>

using namespace std;

#define size(x) (int)size(x)

const int Mod = 998244353;

void add(int &x, const int &y){
	x += y;
	
	if ( x >= Mod ) x -= Mod;
}

int binPow(int x, int y){
	int res = 1;
	
	for (; y > 0; x = x * 1LL * x % Mod, y >>= 1 ){
		if ( y & 1 ) res = res * 1LL * x % Mod;
	}
	
	return res;
}

int rev(int n, int k){
	int x = 0;
	
	for ( int i = 0; i < k; i++ ){
		if ( n >> i & 1 ) x |= 1 << (k - i - 1);
	}
	
	return x;
}

void DFT(vector <int> &c){
	int n = size(c), lg = __lg(n);
	
	for ( int i = 0; i < n; i++ ){
		int j = rev(i, lg);
		
		if ( i < j ) swap(c[j], c[i]);
	}
	
	for ( int b = 1; b <= lg; b++ ){
		int k = 1 << b, w = binPow(3, (Mod - 1) / k);
		
		for ( int i = 0; i < n; i += k ){
			int pw = 1;
			
			for ( int j = i; j < i + k / 2; j++ ){
				int u = c[j], v = c[j + k / 2];
				
				c[j] = (u + v * 1LL * pw) % Mod;
				c[j + k / 2] = (u - v * 1LL * pw % Mod + Mod) % Mod;
				
				pw = pw * 1LL * w % Mod;
			}
		}
	}
}

vector <int> convolution(vector <int> A, vector <int> B){
	if ( size(A) <= 20 ){
		vector <int> C(size(A) + size(B) - 1);
		
		for ( int i = 0; i < size(A); i++ ){
			for ( int j = 0; j < size(B); j++ ){
				add(C[i + j], A[i] * 1LL * B[j] % Mod);
			}
		}
		
		return C;
	}
	
	int n = 1 << (__lg(size(A) + size(B) - 2) + 1);
	
	A.resize(n), B.resize(n);
	
	DFT(A), DFT(B);
	
	for ( int i = 0; i < n; i++ ) A[i] = A[i] * 1LL * B[i] % Mod;
	
	DFT(A);
	
	for ( int i = 1; i < n / 2; i++ ) swap(A[i], A[n - i]);
	
	int inv = binPow(n, Mod - 2);
	
	for ( auto &x: A ) x = x * 1LL * inv % Mod;
	
	return A;
}

signed main(){
	int n; cin >> n;
	
	if ( n == 1 ) return cout << "1\n", 0;
	
	vector <int> fact(1, 1);
	
	while ( size(fact) <= n ) fact.push_back(fact.back() * 1LL * size(fact) % Mod);
	
	vector <int> pw = {1, 10, 100, 1000, 10000, 100000}, A;
	
	for ( int x = 1; x <= n; x++ ){
		bool flag = false;
		
		for ( auto &y: pw ){
			if ( x == y ) flag = true;
		}
		
		if ( !flag ) A.push_back(pw[size(to_string(x))]);
	}
	
	auto dnc = [&](auto dnc, int l, int r) -> vector <int>{
		if ( l == r ) return {1, A[l]};
		
		int m = (l + r) / 2;
		
		return convolution(dnc(dnc, l, m), dnc(dnc, m + 1, r));
	};
	
	vector <int> c = dnc(dnc, 0, size(A) - 1), sum(6);

	for ( int b = 0; b < 6; b++ ){
		if ( pw[b] > n ) break;
		
		vector <int> tmp = {1};
		
		for ( int j = 0; j < 6; j++ ){
			if ( b != j && pw[j] <= n ){
				tmp = convolution({1, pw[j + 1]}, tmp);
			}
		}
		
		tmp = convolution(tmp, c);
		
		for ( int k = 0; k < n; k++ ){
			add(sum[b], tmp[k] * 1LL * fact[k] % Mod * fact[n - k - 1] % Mod);
		}
	}
	
	int ans = 0;
	
	for ( int x = 1; x <= n; x++ ){
		add(ans, sum[size(to_string(x)) - 1] * 1LL * x % Mod);
	}
	
	cout << ans << '\n';
}
