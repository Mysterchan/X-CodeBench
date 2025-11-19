#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int n, l;
    cin >> n >> l;

    vector<int> d(n - 1);
    long long total_dist = 0;
    unordered_map<int, vector<int>> positions;

    for (int i = 0; i < n - 1; i++) {
        cin >> d[i];
        total_dist += d[i];
        total_dist %= l;
        positions[total_dist].push_back(i + 1);
    }

    if (l % 3 != 0) {
        cout << 0 << endl;
        return 0;
    }

    int length = l / 3;
    int length2 = 2 * length;

    long long result = 0;

    for (const auto& [key, group] : positions) {
        int target1 = (key + length) % l;
        int target2 = (key + length2) % l;

        if (positions.find(target1) != positions.end() && positions.find(target2) != positions.end()) {
            const auto& group1 = positions[target1];
            const auto& group2 = positions[target2];

            for (int i : group) {
                auto it1 = lower_bound(group1.begin(), group1.end(), i + 1);
                auto it2 = lower_bound(group2.begin(), group2.end(), i + 1);

                int count1 = group1.end() - it1; // Count elements greater than i
                int count2 = group2.end() - it2; // Count elements greater than i

                result += count1 * count2;
            }
        }
    }

    cout << result << endl;
    return 0;
}