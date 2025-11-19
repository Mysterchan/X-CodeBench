#include <iostream>
#include <vector>
#include <unordered_map>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    cout << setprecision(15);

    int N;
    cin >> N;

    vector<vector<int>> A(N);
    vector<unordered_map<int, int>> frq(N);

    for (int i = 0; i < N; i++) {
        int K;
        cin >> K;
        A[i].resize(K);
        for (int j = 0; j < K; j++) {
            cin >> A[i][j];
            frq[i][A[i][j]]++;  // Count frequencies directly while reading
        }
    }

    double maxProbability = 0;

    // Choose every pair of dice
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            double sameCount = 0;
            for (const auto& entry : frq[i]) {
                int value = entry.first;
                if (frq[j].count(value)) {
                    sameCount += entry.second * frq[j][value];
                }
            }
            double probability = sameCount / (A[i].size() * A[j].size());
            maxProbability = max(maxProbability, probability);
        }
    }

    cout << maxProbability << endl;

    return 0;
}