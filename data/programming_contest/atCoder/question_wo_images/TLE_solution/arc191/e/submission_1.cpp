#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using pli = pair<ll,int>;
#define AMARI 998244353
#define el '\n'
#define El '\n'
#define YESNO(x) ((x) ? "Yes" : "No")
#define YES YESNO(true)
#define NO YESNO(false)
#define REV_PRIORITY_QUEUE(tp) priority_queue<tp,vector<tp>,greater<tp>>
#define EXIT(x) {cout << (x) << '\n'; return;}
template <typename T> void inline SORT(vector<T> &v){sort(v.begin(),v.end()); return;}
template <typename T> void inline VEC_UNIQ(vector<T> &v){sort(v.begin(),v.end()); v.erase(unique(v.begin(),v.end()),v.end()); return;}
template <typename T> T inline MAX(vector<T> &v){return *max_element(v.begin(),v.end());}
template <typename T> T inline MIN(vector<T> &v){return *min_element(v.begin(),v.end());}
template <typename T> T inline SUM(vector<T> &v){T ans = 0; for(int i = 0; i < (int)v.size(); i++)ans += v[i]; return ans;}
void inline TEST(void){cerr << "TEST" << endl; return;}

class ococo_combination{
private:
    long long N,P;
    vector<long long> kaizyou,gyakugen,gyakugen_kaizyou;
    long long pn = -1,pk = -1;
    ll sum_ans = 0;
public:
    ococo_combination(long long p = 998244353,long long n = 10000000){
        n++;
        N = n; P = p;
        kaizyou.resize(n);
        gyakugen.resize(n);
        gyakugen_kaizyou.resize(n);
        kaizyou[0] = kaizyou[1] = 1;
        gyakugen[0] = gyakugen[1] = 1;
        gyakugen_kaizyou[0] = gyakugen_kaizyou[1] = 1;
        for(int i = 2; i < n; i++){
            kaizyou[i] = kaizyou[i - 1] * i % p;
            gyakugen[i] = p - gyakugen[p % i] * (p / i) % p;
            gyakugen_kaizyou[i] = gyakugen_kaizyou[i - 1] * gyakugen[i] % p;
        }
    }
    long long binom(int n,int k){
        if(n < k || n < 0 || k < 0)return 0LL;
        long long ans = kaizyou[n];
        long long temp = gyakugen_kaizyou[n - k];
        temp *= gyakugen_kaizyou[k]; temp %= P;
        ans *= temp; ans %= P;
        return ans;
    }

    long long factorial(int n){
        assert(n < N);
        if(n < 0)return 0LL;
        return kaizyou[n];
    }

    long long sum(int n,int k){
        if(pn == -1 || abs(n - pn) + abs(k - pk) >= k){
            sum_ans = 0;
            for(int i = 0; i <= k; i++){
                sum_ans += binom(n,i);
                if(sum_ans >= P)sum_ans -= P;
            }
            pn = n; pk = k;
            return sum_ans;
        }
        while(n > pn){
            sum_ans = 2LL * sum_ans - binom(pn,pk);
            if(sum_ans < 0)sum_ans += P;
            if(sum_ans >= P)sum_ans -= P;
            pn++;
        }
        while(n < pn){
            ll temp = sum_ans + binom(pn - 1,pk);
            if(temp % 2)temp += P;
            sum_ans = temp / 2;
            pn--;
        }
        while(k < pk){
            sum_ans -= binom(pn,pk);
            if(sum_ans < 0)sum_ans += P;
            pk--;
        }
        while(k > pk){
            pk++;
            sum_ans += binom(pn,pk);
            if(sum_ans >= P)sum_ans -= P;
        }
        return sum_ans;
    }
    long long catalan(int n){
        ll ans = kaizyou[2 * n];
        ans *= gyakugen_kaizyou[n + 1]; ans %= P;
        ans *= gyakugen_kaizyou[n]; ans %= P;
        return ans;
    }
};

vector<ll> ococo_ntt998(vector<ll> & a,int cnt,bool inv = false){
    int n = (int)a.size();
    if(n == 1){
        return a;
    }
    static vector<ll> v = {1,998244352,911660635,372528824,929031873,452798380,922799308,781712469,476477967,166035806,258648936,584193783,63912897,350007156,666702199,968855178,629671588,24514907,996173970,363395222,565042129,733596141,267099868,15311432};
    static vector<ll> vg = {1,998244352,86583718,509520358,337190230,87557064,609441965,135236158,304459705,685443576,381598368,335559352,129292727,358024708,814576206,708402881,283043518,3707709,121392023,704923114,950391366,428961804,382752275,469870224};

    vector<ll> even(n / 2),odd(n / 2);
    for(int i = 0; i < n; i++){
        if(i & 1)odd[i / 2] = a[i];
        else even[i / 2] = a[i];
    }
    even = ococo_ntt998(even,cnt - 1,inv);
    odd = ococo_ntt998(odd,cnt - 1,inv);
    
    vector<ll> ans(n);
    
    ll temp = 1;
    int idx = 0;
    int halfn = n / 2;
    for(int i = 0; i < n; i++){
        ans[i] = even[idx] + (temp * odd[idx] % 998244353);
        idx++; if(idx == halfn)idx = 0;

        if(ans[i] >= 998244353)ans[i] -= 998244353;
        if(inv)temp *= vg[cnt];
        else temp *= v[cnt];
        temp %= 998244353;
    }
    return ans;
}

vector<ll> ococo_convolution998(vector<ll> a,vector<ll> b){
    auto beki = [=](ll a,ll b){
        ll ans = 1,temp = a;
        while(b){
            if(b & 1){
                ans *= temp;
                ans %= 998244353;
            }
            temp *= temp;
            temp %= 998244353;
            b /= 2;
        }
        return ans;
    };
    int n = 1;
    int idx = 0;
    while(n < (int)a.size() + (int)b.size()){
        n *= 2;
        idx++;
    }
    a.resize(n,0LL);
    b.resize(n,0LL);
    a = ococo_ntt998(a,idx,false);
    b = ococo_ntt998(b,idx,false);
    vector<ll> ans(n);
    for(int i = 0; i < n; i++)ans[i] = (a[i] * b[i]) % 998244353;
    ans = ococo_ntt998(ans,idx,true);
    ll temp = beki(n,998244351);
    for(int i = 0; i < n; i++){
        ans[i] *= temp;
        ans[i] %= 998244353;
    }
    return ans;
}

vector<ll> beki(vector<ll> a,ll b){
    vector<ll> ans = {1};
    vector<ll> temp = a;
    while(b){
        if(b % 2){
            ans = ococo_convolution998(ans,temp);
        }
        temp = ococo_convolution998(temp,temp);
        b /= 2;
    }
    return ans;
}
    

#define MULTI_TEST_CASE false
void solve(void){
    int n;
    ll x,y;
    cin >> n >> x >> y;
    vector<ll> a(n),b(n);
    for(int i = 0; i < n; i++){
        cin >> a[i] >> b[i];
    }
    int even = 0,odd = 0;
    if(x % 2 == y % 2 || MAX(a) == 0){
        vector<ll> c(n);
        for(int i = 0; i < n; i++){
            c[i] = a[i] * (x + 1) + b[i];
        }
        for(int i = 0; i < n; i++){
            if(c[i] % 2 == 0)even++;
            if(c[i] % 2 == 1)odd++;
        }
        ll ans = 0LL;

        ococo_combination comb;

        for(int i = 0; i <= odd; i++){
            if(i <= odd - i)continue;
            ans += comb.binom(odd,i);
            if(ans >= AMARI)ans -= AMARI;
        }

        for(int i = 0; i < even; i++){
            ans *= 2;
            ans %= AMARI;
        }
        cout << ans << El;
        return;
    }
    if(x % 2 != y % 2){
        int ta = 0,ao = 0,fi = 0,se = 0;
        for(int i = 0; i < n; i++){
            if(a[i] == 0){
                if(b[i] % 2 == 1)fi++;
                if(b[i] % 2 == 0)se++;
            }
            if(a[i] == 1){
                if(b[i] % 2 == 0 && x % 2 == 0)ta++;
                if(b[i] % 2 == 0 && y % 2 == 0)ao++;
                if(b[i] % 2 == 1)fi++;
            }
            if(a[i] >= 2){
                if(x % 2 == 0)ta++;
                if(y % 2 == 0)ao++;
            }
        }
        vector<ll> x1 = {1,1};
        vector<ll> x2 = {1,0,1};
        vector<ll> xx1 = beki(x1,ao + ta);
        vector<ll> xx2 = beki(x2,fi);
        vector<ll> x3 = ococo_convolution998(xx1,xx2);
        ll ans = 0;
        for(int i = ao + fi + 1; i < (int)x3.size(); i++){
            ans += x3[i];
            if(ans >= AMARI)ans -= AMARI;
        }
        for(int i = 0; i < se; i++){
            ans *= 2;
            if(ans >= AMARI)ans -= AMARI;
        }
        cout << ans << el;
    }
    
    return;
}

void calc(void){
    return;
}

signed main(void){
    cin.tie(nullptr);
    ios::sync_with_stdio(false);
    calc();
    int t = 1;
    if(MULTI_TEST_CASE)cin >> t;
    while(t--){
        solve();
    }
    return 0;
}