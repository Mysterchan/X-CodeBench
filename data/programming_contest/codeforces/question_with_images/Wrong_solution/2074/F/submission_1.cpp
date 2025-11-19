#include<bits/stdc++.h>
#define rep(i,a,b) for(int i=(a);i<=(b);++i)
using namespace std;
using ui = unsigned; using db = long double; using ll = long long; using ul = unsigned long long;
using vi = vector<int>; using vll = vector<ll>;
template<class T1, class T2> istream &operator>>(istream &cin, pair<T1, T2> &a) { return cin >> a.first >> a.second; }
template <std::size_t Index = 0, typename... Ts> typename std::enable_if<Index == sizeof...(Ts), void>::type tuple_read(std::istream &is, std::tuple<Ts...> &t) { }
template <std::size_t Index = 0, typename... Ts> typename std::enable_if < Index < sizeof...(Ts), void>::type tuple_read(std::istream &is, std::tuple<Ts...> &t) { is >> std::get<Index>(t); tuple_read<Index + 1>(is, t); }
template <typename... Ts>std::istream &operator>>(std::istream &is, std::tuple<Ts...> &t) { tuple_read(is, t); return is; }
template<class T1> istream &operator>>(istream &cin, valarray<T1> &a);
template<class T1> istream &operator>>(istream &cin, vector<T1> &a) { for (auto &x : a) cin >> x; return cin; }
template<class T1> istream &operator>>(istream &cin, valarray<T1> &a) { for (auto &x : a) cin >> x; return cin; }
using i128 = __int128;
istream &operator>>(istream &cin, i128 &x) { bool flg = 0; x = 0; static string s; cin >> s; if (s[0] == '-') flg = 1, s = s.substr(1); for (char c : s) x = x * 10 + (c - '0'); if (flg) x = -x; return cin; }
ostream &operator<<(ostream &cout, i128 x) { static char s[60]; if (x < 0) cout << '-', x = -x; int tp = 1; s[0] = '0' + (x % 10); while (x /= 10) s[tp++] = '0' + (x % 10); while (tp--) cout << s[tp]; return cout; }
template<class T1, class T2> ostream &operator<<(ostream &cout, const pair<T1, T2> &a) { return cout << a.first << ' ' << a.second; }
template<class T1, class T2> ostream &operator<<(ostream &cout, const vector<pair<T1, T2>> &a) { for (auto &x : a) cout << x << '\n'; return cout; }
template<class T1> ostream &operator<<(ostream &cout, vector<T1> a) { int n = a.size(); if (!n) return cout; cout << a[0]; for (int i = 1; i < n; i++) cout << ' ' << a[i]; return cout; }
template<class T1> ostream &operator<<(ostream &cout, const valarray<T1> &a) { int n = a.size(); if (!n) return cout; cout << a[0]; for (int i = 1; i < n; i++) cout << ' ' << a[i]; return cout; }
template<class T1> ostream &operator<<(ostream &cout, const vector<valarray<T1>> &a) { int n = a.size(); if (!n) return cout; cout << a[0]; for (int i = 1; i < n; i++) cout << '\n' << a[i]; return cout; }
template<class T1> ostream &operator<<(ostream &cout, const vector<vector<T1>> &a) { int n = a.size(); if (!n) return cout; cout << a[0]; for (int i = 1; i < n; i++) cout << '\n' << a[i]; return cout; }
#define x1 x114514
#define y1 y114514
#define x2 x1919810
#define y2 y1919810
#define int long long
int ans,x1,y1,x2,y2;
void calc(int l,int r,int t){
	if(l==0){
			for(int f=0;f<=t+1;++f){
				if(l+(1<<f)>r or f==t+1){
					--f;++ans;
					l+=(1<<f);
					break;
				}
			}
	}
	for(int f=0;f<=t;++f){
		if(l&(1<<f)){
			if(l+(1<<f)<=r){
				ans+=1<<(t-f);
				l+=(1<<f);
			}else break;
		}
	}
	for(int f=0;f<=t;++f){
		if(r&(1<<f)){
			if(l+(1<<f)<=r){
				ans+=1<<(t-f);
				r-=(1<<f);
			}else break;
		}
	}
	ans+=(r-l)/(1<<t);
}
inline void solve(){
	cin>>x1>>x2>>y1>>y2;
	ans=0;
	bool t=0;
	while(x1!=x2){
		if(x1==0){
			for(int f=0;f<30;++f){
				if(x1+(1<<f)>x2){
					--f;
					calc(y1,y2,f);
					x1+=(1<<f);
					break;
				}
			}
		}
		for(int f=0;f<30;++f){
			if(x1&(1<<f) or x1==0){
				if(x1+(1<<f)>x2){
					t=1;
					break;
				}else{
					calc(y1,y2,f);
					x1+=(1<<f);
				}
			}
		}
		if(t)break;
	}
	while(x1<x2){
		for(int f=30;~f;--f){
			if(x1+(1<<f)<=x2){
				calc(y1,y2,f);
				x1+=(1<<f);
			}
		}
	}
	cout<<ans<<endl;
}
signed main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	int T=1;
	cin>>T;
	for(;T--;)solve();
	return 0;
}
