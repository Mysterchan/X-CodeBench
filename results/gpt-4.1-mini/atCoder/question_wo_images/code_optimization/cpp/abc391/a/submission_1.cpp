#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    unordered_map<string, string> opposite = {
        {"N", "S"}, {"S", "N"},
        {"E", "W"}, {"W", "E"},
        {"NE", "SW"}, {"SW", "NE"},
        {"NW", "SE"}, {"SE", "NW"}
    };

    string D;
    cin >> D;
    cout << opposite[D] << "\n";

    return 0;
}