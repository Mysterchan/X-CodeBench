#include <bits/stdc++.h>
using namespace std;

const int N = 4e5 + 5;
int n, m, q;
pair<int, int> a[N];
vector<int> l[N], r[N]; // left and right road holders
int f[N];

bool can_satisfy(int left, int right) {
    int requirement = 0; 
    for (int i = left; i <= right; i++) {
        int start = a[i].first;
        int end = a[i].second;
        requirement++;
        
        // Check for overlaps
        for (auto &x : r[start]) {
            if (x >= start) {
                return false; // Not satisfy stamina for person
            }
        }
        for (auto &x : l[end]) {
            if (x <= end) {
                return false; // Not satisfy stamina for person
            }
        }
        // Store left and right road independence
        l[start].push_back(end);
        r[end].push_back(start);
    }

    return true; // If all checks passed
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m >> q;

    for (int i = 1; i <= m; i++) {
        int start, end;
        cin >> start >> end;
        if (start > end) swap(start, end);
        a[i] = {start, end};
    }

    for (int i = 1; i <= m; i++) {
        f[i] = i; 
        for (int j = i - 1; j > 0; j--) {
            if (!can_satisfy(j, i)) {
                f[i] = j + 1; // Failing the requirement
                break;
            }
        }
    }

    while(q--) {
        int l_query, r_query;
        cin >> l_query >> r_query;
        cout << (f[r_query] <= l_query ? "Yes" : "No") << endl;
    }

    return 0;
}
