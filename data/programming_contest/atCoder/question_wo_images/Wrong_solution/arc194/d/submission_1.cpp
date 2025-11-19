#include <ios>
#include <iostream>
#include <ostream>
#include <set>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>
#include <queue>
#include <array>
#include <unordered_map>
#include <stack>
#include <iomanip>

#define int long long

using namespace std;

const int maxn = 5005;
const int mod = 998244353;
int fac[maxn];

int binpow(int a, int b) {
    if (b == 0) return 1;
    if (b%2==1) return (binpow(a, b-1)*a)%mod;
    int v = binpow(a, b/2);
    return (v*v)%mod;
}
int inverse(int a) {
    return binpow(a, mod-2);
}

int n;
string s;

string sort(int l, int r) {
    if (r-l+1 == 2) return "()";
    int prev = l-1;
    int sum = 0;
    vector<string> vec;
    bool leaf = false;
    for (int i = l; i <= r; i++) {
        if (s[i] == '(') sum++;
        else sum--;
        if (sum == 0) {
            if (i == r && prev == l-1) {
                leaf = true;
            } else {
                vec.push_back(sort(prev + 1, i));
                prev = i;
            }
        }
    }
    if (leaf) {
        return "(" + sort(l+1, r-1) + ")";
    }
    sort(vec.begin(), vec.end());
    string res;
    for (string x : vec) res += x;
    return res;
}

int f(int l, int r) {
    if (r-l+1 == 2) return 1;
    int prev = l-1;
    int sum = 0;
    vector<string> vec;
    bool leaf = false;
    int res = 1;
    for (int i = l; i <= r; i++) {
        if (s[i] == '(') sum++;
        else sum--;
        if (sum == 0) {
            if (i == r && prev == l-1) {
                leaf = true;
            } else {
                res = (res*f(prev+1, i))%mod;
                vec.push_back(sort(prev + 1, i));
                prev = i;
            }
        }
    }
    if (leaf) {
        return f(l+1,r-1);
    }
    map<string, int> f;
    for (string x : vec) f[x]++;
    res = (res*fac[f.size()])%mod;
    for (pair<string,int> p : f)  res = (res*inverse(fac[p.second]))%mod;
    return res;
}

signed main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    fac[0] = 1;
    for (int i = 1; i < maxn; i++) fac[i] = (fac[i-1]*i)%mod;
    cin >> n >> s;
    s = sort(0, n-1);
    int res = f(0, n-1);
    cout << res << '\n';
}

