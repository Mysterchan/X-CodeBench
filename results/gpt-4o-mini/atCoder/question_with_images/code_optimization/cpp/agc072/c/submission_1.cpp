#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    long long K;
    cin >> N >> K;

    string path = "";
    int i = 1, j = 1;

    long long totalMoves = 0; 

    while (i < N || j < N) {
        long long downMoves = (N - i) * (N - j);
        long long rightMoves = (N - j) * (N - i);

        if (totalMoves + downMoves < K) {
            path += 'D';
            totalMoves += downMoves;
            i++;
        } else {
            path += 'R';
            K -= totalMoves;
            K--;
            j++;
        }
    }

    cout << path << endl;

    return 0;
}