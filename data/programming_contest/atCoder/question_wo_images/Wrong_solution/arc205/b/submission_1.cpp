#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>
#include <algorithm>
#include <utility>
#include <numeric>
#include <tuple>
#include <ranges>
namespace zawa {}
using namespace zawa;
using namespace std;
template <class T, class U>
ostream& operator<<(ostream& os, const pair<T, U>& p) {
    os << '(' << p.first << ',' << p.second << ')';
    return os;
}
template <class T>
ostream& operator<<(ostream& os, const vector<T>& v) {
    for (int i = 0 ; i < ssize(v) ; i++)
        os << v[i] << (i + 1 == ssize(v) ? "" : " ");
    return os;
}
long long mystoll(string s) {
    long long res = 0;
    for (char c : s)
        res = (res * 10) + c - '0';
    return res;
}
int main() {
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(0);
    int N, M;
    cin >> N >> M;
    vector<int> pal(N, (N - 1) & 1);
    for (int i = 0 ; i < M ; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        pal[u] ^= 1;
        pal[v] ^= 1;
    }
    long long ans = 0;
    for (int i = 0 ; i < N ; i++) {
        if (((N - 1) & 1) == pal[i])
            ans += N - 1;
        else
            ans += N - 2;
    }
    ans /= 2;
    cout << ans << '\n';
}
