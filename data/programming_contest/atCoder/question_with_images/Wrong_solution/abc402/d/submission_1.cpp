#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;
    Fenwick(int n = 0) { init(n); }
    void init(int n_) {
        n = n_;
        bit.assign(n + 1, 0);
    }
    void add(int idx, int val) { 
        for (; idx <= n; idx += idx & -idx)
            bit[idx] += val;
    }
    int sumPrefix(int idx) const {
        int res = 0;
        for (; idx > 0; idx -= idx & -idx)
            res += bit[idx];
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    if (!(cin >> N >> M)) return 0;
    vector<pair<int,int>> seg(M);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        seg[i] = {a, b};
    }

    sort(seg.begin(), seg.end(),
         [](const pair<int,int>& x, const pair<int,int>& y){
             if (x.first != y.first) return x.first < y.first;
             return x.second < y.second;
         });

    Fenwick bit(N);
    priority_queue<int, vector<int>, greater<int>> minHeap;
    long long answer = 0;

    int idx = 0;
    while (idx < M) {
        int curStart = seg[idx].first;

        
        while (!minHeap.empty() && minHeap.top() <= curStart) {
            int ended = minHeap.top(); minHeap.pop();
            bit.add(ended, -1);
        }

        
        int nxt = idx;
        while (nxt < M && seg[nxt].first == curStart) ++nxt;

        
        for (int t = idx; t < nxt; ++t) {
            int end = seg[t].second;
            answer += bit.sumPrefix(end - 1);
        }

        
        for (int t = idx; t < nxt; ++t) {
            int end = seg[t].second;
            minHeap.push(end);
            bit.add(end, 1);
        }

        idx = nxt;
    }

    cout << answer << '\n';
    return 0;
}