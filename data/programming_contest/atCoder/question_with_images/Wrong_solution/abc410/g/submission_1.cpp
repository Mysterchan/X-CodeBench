#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    if (!(cin >> N)) return 0;
    vector<pair<int,int>> seg(N);
    for (int i = 0; i < N; ++i) {
        int a,b;  cin >> a >> b;
        if (a < b) seg[i] = {a,b};
        else       seg[i] = {b,a};
    }
    sort(seg.begin(), seg.end(),
         [](const auto& p, const auto& q){ return p.first < q.first; });

    vector<int> tail;
    for (auto &p : seg) {
        int x = -p.second;
        auto it = lower_bound(tail.begin(), tail.end(), x);
        if (it == tail.end()) tail.push_back(x);
        else *it = x;
    }
    cout << (int)tail.size() << "\n";
    return 0;
}
