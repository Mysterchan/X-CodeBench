#include <bits/stdc++.h>
#define _rep(i, x, y) for(int i = x; i <= y; ++i)
#define _req(i, x, y) for(int i = x; i >= y; --i)
#define pb push_back
#define fi first
#define se second
using namespace std;
typedef long long ll;
typedef pair<int, int> PII;

namespace fastio{
    template<typename T> inline void read(T &t){
        T x = 0, f = 1;
        char c = getchar();
        while(!isdigit(c)){
            if(c == '-') f = -f;
            c = getchar();
        }
        while(isdigit(c)) x = x * 10 + c - '0', c = getchar();
        t = x * f;
    }
    template<typename T, typename ... Args> inline void read(T &t, Args&... args){
        read(t);
        read(args...);
    }
};
using namespace fastio;

const int N = 4e5 + 5;
int n, m, q, op[N];
PII a[N];
int f[N];
map<PII, int> mp[2];
int cntl[N], cntr[N];
multiset<int> st[2][N], st2[2][N];
int bad_count;

void ins(int x){
    int l = a[x].fi, r = a[x].se;
    int t = op[x];
    
    if(mp[t ^ 1][a[x]]) bad_count++;
    mp[t][a[x]]++;
    
    int prev_cntl = cntl[l];
    int prev_cntr = cntr[r];
    cntl[l]++, cntr[r]++;
    
    if(prev_cntl > 0 && prev_cntl != mp[t][a[x]] - 1) bad_count++;
    if(prev_cntr > 0 && prev_cntr != mp[t][a[x]] - 1) bad_count++;
    
    _rep(i, l + 1, r - 1){
        if(!st[t][i].empty() && *st[t][i].begin() < l) bad_count++;
        if(!st2[t][i].empty() && *st2[t][i].rbegin() > r) bad_count++;
    }
    
    st[t][r].insert(l);
    st2[t][l].insert(r);
}

void del(int x){
    int l = a[x].fi, r = a[x].se;
    int t = op[x];
    
    st[t][r].erase(st[t][r].find(l));
    st2[t][l].erase(st2[t][l].find(r));
    
    _rep(i, l + 1, r - 1){
        if(!st[t][i].empty() && *st[t][i].begin() < l) bad_count--;
        if(!st2[t][i].empty() && *st2[t][i].rbegin() > r) bad_count--;
    }
    
    int prev_cntl = cntl[l];
    int prev_cntr = cntr[r];
    
    if(prev_cntl > 1 && prev_cntl != mp[t][a[x]]) bad_count--;
    if(prev_cntr > 1 && prev_cntr != mp[t][a[x]]) bad_count--;
    
    cntl[l]--, cntr[r]--;
    mp[t][a[x]]--;
    
    if(mp[t ^ 1][a[x]]) bad_count--;
}

bool is_valid(){
    return bad_count == 0;
}

int main(){
    read(n, m, q);
    _rep(i, 1, m){
        read(a[i].fi, a[i].se);
        op[i] = a[i].fi < a[i].se;
        if(a[i].fi > a[i].se) swap(a[i].fi, a[i].se);
    }
    
    bad_count = 0;
    for(int i = 1, j = 1; i <= m; ++i){
        ins(i);
        while(!is_valid()) del(j++);
        f[i] = j;
    }
    
    _rep(i, 1, q){
        int l, r;
        read(l, r);
        puts(f[r] <= l ? "Yes" : "No");
    }
    return 0;
}