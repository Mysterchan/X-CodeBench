#include <bits/stdc++.h>
using namespace std;
// #define int long long
#define rep(i, j, k) for(int i = (j); i <= (k); i++)
#define per(i, j, k) for(int i = (j); i >= (k); i--)
#define pb emplace_back
#define fi first
#define se second
using vi = vector<int>;
using pi = pair<int, int>;

template<typename T0, typename T1> bool chmin(T0 &x, const T1 &y){
	if(y < x){x = y; return true;} return false;
}
template<typename T0, typename T1> bool chmax(T0 &x, const T1 &y){
	if(x < y){x = y; return true;} return false;
}

template<typename T> void debug(char *s, T x){
	cerr << s <<" = "<< x <<endl;
}
template<typename T, typename ...Ar> void debug(char *s, T x, Ar... y){
	int dep = 0;
	while(!(*s == ',' && dep == 0)){
		if(*s == '(') dep++;
		if(*s == ')') dep--;
		cerr << *s++;
	}
	cerr <<" = "<< x <<",";
	debug(s + 1, y...);
}
#define gdb(...) debug((char*)#__VA_ARGS__, __VA_ARGS__)

using u32 = uint32_t;
using u64 = uint64_t;
constexpr int mod = 998244353;
struct mint{
	u32 x;
	
	mint(): x(0){}
	mint(int _x){
		_x %= mod;
		if(_x < 0) _x += mod;
		x = _x;
	}

	u32 val()const {
		return x;
	}
	mint qpow(int y = mod - 2)const {
		assert(y >= 0);
		mint t = *this, res = 1;
		while(y){
			if(y % 2) res *= t;
			t *= t;
			y /= 2;
		}
		return res;
	}

	mint& operator += (const mint &B){
		if((x += B.x) >= mod) x -= mod;
		return *this;
	}
	mint& operator -= (const mint &B){
		if((x -= B.x) >= mod) x += mod;
		return *this;
	}
	mint& operator *= (const mint &B){
		x = (u64)x * B.x % mod;
		return *this;
	}
	mint& operator /= (const mint &B){
		return *this *= B.qpow();
	}
	friend mint operator + (const mint &A, const mint &B){
		return mint(A) += B;
	}
	friend mint operator - (const mint &A, const mint &B){
		return mint(A) -= B;
	}
	friend mint operator * (const mint &A, const mint &B){
		return mint(A) *= B;
	}
	friend mint operator / (const mint &A, const mint &B){
		return mint(A) /= B;
	}
	mint operator - ()const {
		return mint() - *this;
	}
};

constexpr int LG = 21, S = 1 << LG;
vector<mint> P, fac, ifac, iv, ip2;

auto INIT = [](){
	P.resize(S);
	rep(i, 0, LG - 1){
		mint stp = mint(3).qpow(mod >> (i + 1));
		P[1 << i] = 1;
		rep(j, (1 << i) + 1, (2 << i) - 1){
			P[j] = P[j - 1] * stp;
		}
	}

	fac.resize(S);
	ifac.resize(S);
	iv.resize(S);
	fac[0] = iv[0] = 1;
	rep(i, 1, S - 1){
		fac[i] = fac[i - 1] * i;
	}
	ifac[S - 1] = 1 / fac[S - 1];
	per(i, S - 1, 1){
		ifac[i - 1] = ifac[i] * i;
		iv[i] = ifac[i] * fac[i - 1];
	}

	ip2.resize(LG + 1);
	ip2[0] = 1;
	rep(i, 1, LG){
		ip2[i] = ip2[i - 1] / 2;
	}
	
	return true;
}();

struct poly : vector<mint>{
	using vector<mint>::vector;
	
	void DIF(int lg){
		for(int i = 1 << (lg - 1); i ; i /= 2){
			for(int j = 0; j < (1 << lg); j += 2 * i){
				rep(k, 0, i - 1){
					mint A = (*this)[j + k], B = (*this)[j + k + i];
					(*this)[j + k] = A + B, (*this)[j + k + i] = (A - B) * P[i + k];
				}
			}
		}
	}

	void DIT(int lg){
		for(int i = 1; i < (1 << lg); i *= 2){
			for(int j = 0; j < (1 << lg); j += 2 * i){
				rep(k, 0, i - 1){
					mint A = (*this)[j + k], B = (*this)[j + k + i] * P[i + k];
					(*this)[j + k] = A + B, (*this)[j + k + i] = A - B;
				}
			}
		}
		reverse(this -> begin() + 1, this -> end());
	}

	friend poly der(const poly &A){
		poly res = A;
		rep(i, 1, (int)res.size() - 1){
			res[i - 1] = res[i] * i;
		}
		res.pop_back();
		return res;
	}

	friend poly ints(const poly &A){
		poly res = A;
		res.pb();
		per(i, (int)res.size() - 1, 0){
			res[i] = res[i - 1] * iv[i];
		}
		res[0] = 0;
		return res;
	}

	poly& operator += (const poly &B){
		if(B.size() > this -> size()){
			this -> resize(B.size());
		}
		rep(i, 0, (int)B.size() - 1){
			(*this)[i] += B[i];
		}
		return *this;
	}

	friend poly operator + (const poly &A, const poly &B){
		return poly(A) += B;
	}

	poly& operator -= (const poly &B){
		if(B.size() > this -> size()){
			this -> resize(B.size());
		}
		rep(i, 0, (int)B.size() - 1){
			(*this)[i] -= B[i];
		}
		return *this;
	}

	friend poly operator - (const poly &A, const poly &B){
		return poly(A) -= B;
	}

	friend poly operator * (const mint &k, const poly &A){
		poly res = A;
		for(auto &x:res) x *= k;
		return res;
	}

	poly& operator *= (const poly &B){
		auto sz = this -> size();
		*this = conv(*this, B);
		this -> resize(sz);
		return *this;
	}

	friend poly operator * (const poly &A, const poly &B){
		return poly(A) *= B;
	}

	poly& operator /= (const poly &B){
		auto sz = this -> size();
		*this = conv(*this, inv(B));
		this -> resize(sz);
		return *this;
	}

	friend poly operator / (const poly &A, const poly &B){
		return poly(A) /= B;
	}

	friend poly conv(const poly &_A, const poly &_B){
		if(_A.size() <= 64 || _B.size() <= 64){
			poly res(_A.size() + _B.size() - 1);
			rep(i, 0, (int)_A.size() - 1){
				rep(j, 0, (int)_B.size() - 1){
					res[i + j] += _A[i] * _B[j];
				}
			}
			return res;
		}

		poly A = _A, B = _B;
		int len = A.size() + B.size() - 1;
		int lg = __lg(len * 2 - 1);
		A.resize(1 << lg), B.resize(1 << lg);
		A.DIF(lg), B.DIF(lg);
		rep(i, 0, (1 << lg) - 1){
			A[i] *= B[i];
		}
		A.DIT(lg);
		A.resize(len);
		for(auto &x:A) x *= ip2[lg];
		return A;
	}

	friend poly inv(const poly &A){
		assert(A[0].val() != 0);
		poly res{mint(1) / A[0]};
		while(res.size() < A.size()){
			int n = res.size(), lg = __lg(n * 4);
			poly buf(1 << lg);
			copy(res.begin(), res.end(), buf.begin());
			buf.DIF(lg);

			poly tmp{A.begin(), A.begin() + min(n * 2, (int)A.size())};
			tmp.resize(n * 4);
			tmp.DIF(lg);
			rep(i, 0, n * 4 - 1) tmp[i] *= buf[i] * buf[i];
			tmp.DIT(lg);

			res.resize(n * 2);
			rep(i, 0, n * 2 - 1){
				res[i] = 2 * res[i] - tmp[i] * ip2[lg];
			}
		}
		res.resize(A.size());
		return res;
	}


	// O(n \log^2 n)
	friend poly exp(const poly &A){
		assert(A[0].val() == 0);
		int n = A.size();
		int lg = __lg(n * 2 - 1);

		poly a = A, res(A.size());
		rep(i, 0, (int)a.size() - 1) a[i] *= i;
		a.resize(1 << lg);

		vector<poly> pre(lg + 1);
		rep(i, 8, lg){
			pre[i].insert(pre[i].end(), a.begin(), a.begin() + (1 << i));
			pre[i].DIF(i);
		}

		res[0] = 1;
		auto slv = [&](auto &self, int l, int r)->void {
			if(r - l <= 128){
				rep(i, l, r - 1){
					rep(j, l, i - 1){
						res[i] += res[j] * a[i - j];
					}
					if(i > 0) res[i] *= iv[i];
				}
				return;
			}
			int mid = (l + r) / 2;
			self(self, l, mid);

			int _lg = __lg((r - l) * 2 - 1);
			poly tmp(res.begin() + l, res.begin() + mid);
			tmp.resize(1 << _lg);
			tmp.DIF(_lg);
			rep(i, 0, (1 << _lg) - 1) tmp[i] *= pre[_lg][i];
			tmp.DIT(_lg);
			rep(i, mid, r - 1) res[i] += tmp[i - l] * ip2[lg];
			self(self, mid, r);
		};
		slv(slv, 0, n);
		return res;
	}
	
	friend poly ln(const poly &A){
		assert(A[0].val() == 1);
		poly res = der(A) / A;
		return ints(res);
	}
	
	friend poly sqrt(const poly &A){
		assert(A[0].val() == 1);
		return exp(ip2[1] * ln(A));
	}

	friend poly qpow(const poly &A, mint k){
		if(k.val() == 0){
			poly res(A.size());
			res[0] = 1;
			return res;
		}

		auto it = A.begin();
		while(it != A.end() && it -> val() == 0){
			it ++;
		}
		int len = (it - A.begin()) * k.val();
		if(len >= (int)A.size()){
			return poly(A.size());
		} else{
			poly a{it, it + (A.size() - len)};
			mint t = a[0].qpow(k.val());
			a = t * exp(k * ln(1 / a[0] * a));
			a.insert(a.begin(), len, mint());
			return a;
		}
	}
};

const int N = 3e5 + 5;
const int BL = 1000;

mint C(int m, int n){
	return n < 0 || n > m? 0: fac[m] * ifac[n] * ifac[m - n];
}

mint F(int m, int n){
	return (n + m) % 2? 0: C(m, (m - n) / 2);
}

signed main(){
	ios::sync_with_stdio(0);
	cin.tie(0);

	auto solve0 = [&](int s, int t, int n, int m){
		poly res(m + 1);
		poly f(n);
		f[s] = 1;
		res[0] = f[t];
		poly tmp(n);
		rep(i, 1, m){
			copy(f.begin(), f.end(), tmp.begin());
			rep(j, 0, n - 2){
				tmp[j + 1] += f[j];
			}
			rep(j, 1, n - 1){
				tmp[j - 1] += f[j];
			}
			swap(f, tmp);
			res[i] = f[t];
		}
		return res;
	};
	auto solve1 = [&](int s, int t, int n, int m){
		int l = (n + 1) * 2;
		poly tmp(m + 1);
		rep(k, 0, m){
			tmp[k] = F(k, t - s);
			for(int j = t + l; j <= s + k; j += l){
				tmp[k] += F(k, j - s);
			}
			for(int j = t - l; j >= s - k; j -= l){
				tmp[k] += F(k, j - s);
			}
			for(int j = n * 2 - t; j <= s + k; j += l){
				tmp[k] -= F(k, j - s);
			}
			for(int j = (-1) * 2 - t; j >= s - k; j -= l){
				tmp[k] -= F(k, j - s);
			}
		}
		poly coef(m + 1);
		rep(i, 0, m){
			coef[i] = ifac[i];
			tmp[i] *= ifac[i];
		}
		poly res = tmp * coef;
		rep(i, 0, m){
			res[i] *= fac[i];
		}
		return res;
	};
	auto solve = [&](int s, int t, int n, int m){
		return n <= BL? solve0(s, t, n, m): solve1(s, t, n, m);
	};

	int n, m, t, x0, y0, x1, y1;
	cin >> n >> m >> t >> x0 >> y0 >> x1 >> y1;
	x0 -= 1, x1 -= 1;
	y0 -= 1, y1 -= 1;

	auto f = solve(x0, x1, n, t);
	auto g = solve(y0, y1, m, t);

	mint ans = 0;
	rep(i, 0, t){
		ans += ((t - i) % 2? -1: 1) * C(t, i) * f[i] * g[i];
	}
	cout << ans.val() <<'\n';
}
