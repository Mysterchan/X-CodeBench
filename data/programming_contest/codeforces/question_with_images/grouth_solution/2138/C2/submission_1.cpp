#include <bits/stdc++.h>
using namespace std;

namespace std {

	template<class Fun>
	class y_combinator_result {
		Fun fun_;
	public:
		template<class T>
		explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}
	
		template<class ...Args>
		decltype(auto) operator()(Args &&...args) {
			return fun_(std::ref(*this), std::forward<Args>(args)...);
		}
	};
	
	template<class Fun>
	decltype(auto) y_combinator(Fun &&fun) {
		return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun));
	}
	
}
	
void solve(){
	int N, K;
	cin >> N >> K;
	vector<int> par(N);
	vector<vector<int> > ch(N);
	vector<int> d(N);
	for(int i = 1; i < N; i++){
		cin >> par[i];
		par[i]--;
		ch[par[i]].push_back(i);
	}
	int minleaf = N+1;
	vector<int> freq(N);
	for(int i = 0; i < N; i++){
		if(i > 0){
			d[i] = d[par[i]] + 1;
		}
		freq[d[i]]++;
		if(ch[i].size() == 0){
			minleaf = min(minleaf, d[i]);
		}
	}
	freq.resize(minleaf+1);
	int s = 0;
	int e = (int)freq.size() + 1;
	while(s + 1 < e){
		int m = (s+e) / 2;
		vector<int> a(freq.begin(), freq.begin() + m);
		using bs = bitset<200001>;

		map<int,int> afreq;
		for(int x : a) afreq[x]++;

		bs b;
		b[0] = 1;
		for(auto [x, f] : afreq){
			for(int i = 0; (1 << i) <= f; i++){
				if(f & (1 << i)){
					b = b | (b << x);
					for(int j = 0; j < i; j++){
						b = b | (b << (x << j));
					}
				}
			}
		}
		int tot = 0;
		for(int x : a) tot += x;
		bool ok = false;
		for(int j = 0; j <= tot; j++){
			if(b[j] && j <= K && tot-j <= N-K) ok = true;
		}
		if(ok){
			s = m;
		} else {
			e = m;
		}
	}

	cout << s << '\n';
}

int main(){
	ios_base::sync_with_stdio(false), cin.tie(nullptr);
	int T;
	cin >> T;
	while(T--) solve();
}
