#include<bits/stdc++.h>
using namespace std;
#define int long long
typedef pair<int,int> PII;

const int N=2005;

int n;
int a[N], b[N];
map<double, int> slopeCount;
map<PII, int> midPointCount;

signed main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> a[i] >> b[i];

    int ans = 0, totalPairs = 0;

    for(int i = 1; i <= n; i++) {
        for(int j = i + 1; j <= n; j++) {
            if (a[i] == a[j]) {
                // Vertical line, handle as special case
                slopeCount[1e9]++;
                continue;
            }

            double slope = static_cast<double>(b[i] - b[j]) / (a[i] - a[j]);
            slopeCount[slope]++;
            
            // Calculate midpoint
            PII midPoint = {a[i] + a[j], b[i] + b[j]};
            totalPairs += midPointCount[midPoint];
            midPointCount[midPoint]++;
        }
    }

    for(auto& p : slopeCount) {
        ans += p.second * (p.second - 1) / 2;
    }

    cout << ans + totalPairs << '\n';
    
    return 0;
}