#include <iostream>
using namespace std;
typedef long long ll;

bool isSnakeNumber(ll num) {
    string s = to_string(num);
    char topDigit = s[0];
    for (int j = 1; j < s.size(); j++) {
        if (topDigit <= s[j]) {
            return false;
        }
    }
    return true;
}

int countSnakeNumbers(ll L, ll R) {
    int count = 0;
    ll top = 10;
    
    // Iterate through different top digits from each power of 10
    for (int d = 1; d <= 9; d++) {
        for (ll base = 0; base < 10; base++) {
            if (base >= d) continue; // Skip bases that aren't less than the top digit
            for (ll length = 1; length <= 18; length++) {
                ll snakeNum = d * top + base;
                if (snakeNum >= L && snakeNum <= R) {
                    count++;
                }
                if (snakeNum > R) break; // If snakeNum by this formula exceeds R, break
            }
        }
        top *= 10; // Move to next power of ten
    }
    
    return count;
}

int main(void) {
    ll l, r;
    cin >> l >> r;
    cout << countSnakeNumbers(l, r) << endl;
    return 0;
}