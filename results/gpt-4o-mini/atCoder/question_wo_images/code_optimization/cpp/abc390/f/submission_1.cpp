#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    long long answer = 0;
    unordered_map<int, int> last_position;
    
    for (int L = 0; L < N; L++) {
        last_position.clear();
        int components = 0;

        for (int R = L; R < N; R++) {
            // If the current element is the first occurrence in this window
            if (last_position[A[R]] == 0) {
                components++;
            }
            // Update the last position of the current element
            last_position[A[R]] = R + 1;

            // Count components based on the number of distinct integers in current (L, R)
            answer += components;
        }
    }

    cout << answer << endl;
    return 0;
}