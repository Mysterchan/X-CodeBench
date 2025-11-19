
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    
    for(int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    
    bool isStrictlyIncreasing = true;
    
    for(int i = 1; i < n; ++i) {
        if(a[i] <= a[i - 1]) {
            isStrictlyIncreasing = false;
            break;
        }
    }
    
    std::cout << (isStrictlyIncreasing ? "Yes" : "No") << std::endl;
    return 0;
}
