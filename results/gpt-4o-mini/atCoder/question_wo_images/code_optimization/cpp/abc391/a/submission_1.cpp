#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    unordered_map<string, string> oppositeDirections = {
        {"N", "S"}, {"S", "N"}, {"E", "W"}, {"W", "E"},
        {"NE", "SW"}, {"SW", "NE"}, {"NW", "SE"}, {"SE", "NW"}
    };
    
    string D;
    cin >> D;

    cout << oppositeDirections[D] << endl;
    return 0;
}