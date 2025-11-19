#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> A(3);
  for (int i = 0; i < 3; i++) {
    cin >> A[i];
  }
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3;i++) {
      for (int k = 0; k < 3;i++) {
        if (i == j || i == k || j == k) {
          continue;
        }
        if (i * j == k) {
          cout << "Yes" << endl;
          return 0;
        }
      }
    }
  }
  cout << "No" << endl;
  return 0;
}