#include <bits/stdc++.h>
using namespace std;

template <typename T> void set_min(T& a, const T& b){
	if(b < a) a = b;
}
template <typename T> void set_max(T& a, const T& b){
	if(b > a) a = b;
}

using ll = int64_t;

void solve(){
	int N;
	cin >> N;
	vector<ll> A(N);
	for(int i = 0; i < N; i++) cin >> A[i];
	vector<vector<ll> > dp(N, vector<ll>(N));
	for(int i = N-1; i >= 0; i--){
		for(int j = i+1; j < N; j++){
			for(int k = i; k < j; k++){
				set_max(dp[i][j], dp[i][k] + dp[k+1][j]);
			}
			for(int k = i+1; k < j; k++){
				set_max(dp[i][j], dp[i+1][k-1] + dp[k+1][j-1] + A[i] * A[j] * A[k]);
			}
		}
	}
	cout << dp[0][N-1] << '\n';
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int T;
	cin >> T;
	while(T--) solve();
}
