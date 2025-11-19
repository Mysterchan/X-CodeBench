#include <bits/stdc++.h>
using namespace std;

void solve(){
	int N, X;
	cin >> N >> X;
	X--;
	string S;
	cin >> S;
	int ans = N;
	if(X == 0 || X == N-1){
		ans = 1;
	} else {
		int nl = -1;
		int nr = N+1;
		for(int i = 0; i < X; i++){
			if(S[i] == '#') nl = i;
		}
		for(int i = N-1; i > X; i--){
			if(S[i] == '#') nr = i;
		}
		ans = max(min((X-1)+1, N-nr)+1, min(N-(X+1), nl+1)+1);
	}
	cout << ans << '\n';
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int T;
	cin >> T;
	while(T--) solve();
}
