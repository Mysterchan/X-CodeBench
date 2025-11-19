#include <iostream>
#include <iomanip>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(15);

    int N;
    cin >> N;

    vector<int> K(N);
    vector<unordered_map<int, int>> freq(N);
    vector<int> sizes(N);

    for (int i = 0; i < N; i++) {
        cin >> K[i];
        sizes[i] = K[i];
        for (int j = 0; j < K[i]; j++) {
            int a; cin >> a;
            freq[i][a]++;
        }
    }

    double ans = 0.0;

    // For each pair of dice, compute the probability that they show the same number
    // Probability = sum over all numbers x of (freq[i][x]/K[i]) * (freq[j][x]/K[j])
    // = sum_x freq[i][x]*freq[j][x] / (K[i]*K[j])

    // To optimize, iterate over the smaller frequency map for each pair
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            // Choose the smaller map to iterate
            const auto& small = (freq[i].size() < freq[j].size()) ? freq[i] : freq[j];
            const auto& large = (freq[i].size() < freq[j].size()) ? freq[j] : freq[i];

            long long common = 0;
            for (const auto& p : small) {
                auto it = large.find(p.first);
                if (it != large.end()) {
                    common += (long long)p.second * it->second;
                }
            }

            double prob = (double)common / (sizes[i] * sizes[j]);
            if (prob > ans) ans = prob;
        }
    }

    cout << ans << "\n";

    return 0;
}