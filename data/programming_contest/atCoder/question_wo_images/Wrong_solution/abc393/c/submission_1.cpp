#include <iostream> // cout, endl, cin
#include <string> // string, to_string, stoi
#include <vector> // vector
#include <algorithm> // min, max, swap, sort, reverse, lower_bound, upper_bound
#include <utility> // pair, make_pair
#include <tuple> // tuple, make_tuple
#include <cstdint> // int64_t, int*_t
#include <cstdio> // printf
#include <map> // map
#include <queue> // queue, priority_queue
#include <set> // set
#include <stack> // stack
#include <deque> // deque
#include <unordered_map> // unordered_map
#include <unordered_set> // unordered_set
#include <bitset> // bitset
#include <cctype> // isupper, islower, isdigit, toupper, tolower
#include <cmath> // pow, sqrt
#include <iomanip> // setprecision
#define int int64_t
#define double long double
using namespace std;
signed main() {
    int n, m; cin >> n >> m;
    int ans = 0;
    set<pair<int, int>> st;
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v;
        if (u == v) ans++;
        if (u > v) swap(u, v);
        if (st.count({ u,v })) ans++;
        else st.insert({ u,v });
    }
    cout << ans << endl;
    return 0;
}