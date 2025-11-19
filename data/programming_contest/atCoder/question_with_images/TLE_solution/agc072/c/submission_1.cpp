#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int N;
    long long K;
    cin >> N >> K;
    
    vector<vector<long long>> visited(N + 1, vector<long long>(N + 1, 0));
    
    for (long long exercise = 1; exercise <= K; exercise++) {
        string path = "";
        int i = 1, j = 1;
        
        visited[i][j]++;
        
        for (int move = 0; move < 2 * N - 2; move++) {
            bool canGoDown = (i < N);
            bool canGoRight = (j < N);
            
            if (canGoDown && canGoRight) {
                long long downVisits = visited[i + 1][j];
                long long rightVisits = visited[i][j + 1];
                
                if (downVisits < rightVisits) {
                    i++;
                    path += 'D';
                } else if (rightVisits < downVisits) {
                    j++;
                    path += 'R';
                } else {
                    i++;
                    path += 'D';
                }
            } else if (canGoDown) {
                i++;
                path += 'D';
            } else {
                j++;
                path += 'R';
            }
            
            visited[i][j]++;
        }
        
        if (exercise == K) {
            cout << path << endl;
            return 0;
        }
    }
    
    return 0;
}