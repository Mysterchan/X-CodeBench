#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    unordered_set<int> S;
    vector<int> nums(N);

    for(int i = 0; i < N; i++) {
        cin >> nums[i];
        S.insert(nums[i]);
    }

    int count = 0;
    for(int i = 0; i < N; i++) {
        int B = nums[i];
        for(int d = 1; S.count(B - d) && S.count(B + d); d++) {
            count++;
        }
    }

    cout << count;
    return 0;
}