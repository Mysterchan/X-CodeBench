#include <bits/stdc++.h>

using i64 = long long;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    int n;
    std::cin >> n;
    
    std::vector<int> x(n), y(n);
    for (int i = 0; i < n; i++) {
        std::cin >> x[i] >> y[i];
    }
    
    i64 ans = 0;
    std::vector<std::pair<int, int>> slopes, midpts;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int dx = x[j] - x[i];
            int dy = y[j] - y[i];
            int g = std::gcd(dx, dy);
            dx /= g;
            dy /= g;
            if (dx < 0) {
                dx = -dx;
                dy = -dy;
            }
            slopes.emplace_back(dy, dx);
            int mx = x[j] + x[i];
            int my = y[j] + y[i];
            midpts.emplace_back(mx, my);
        }
    }
    
    std::sort(slopes.begin(), slopes.end());
    std::sort(midpts.begin(), midpts.end());
    
    for (int i = 0, c = 0; i < (int)slopes.size(); i++) {
        ans += c;
        if (i > 0 && slopes[i] == slopes[i - 1]) {
            c++;
        } else {
            c = 0;
        }
    }
    
    for (int i = 0, c = 0; i < (int)midpts.size(); i++) {
        ans -= c;
        if (i > 0 && midpts[i] == midpts[i - 1]) {
            c++;
        } else {
            c = 0;
        }
    }
    
    std::cout << ans << "\n";
    
    return 0;
}
