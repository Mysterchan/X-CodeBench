#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    long r;
    cin >> r;

    long answer = 0;
    long r2 = 2 * r;
    long r2_squared = r2 * r2;
    
    // Count squares in the first quadrant (and on positive axes)
    long max_x = (long)sqrt(r2_squared - 1);
    
    for (long x = 0; x <= max_x; x += 2) {
        long x_plus_1 = x + 1;
        long remaining = r2_squared - x_plus_1 * x_plus_1;
        if (remaining < 0) break;
        
        long y_max = (long)sqrt(remaining);
        long count = (y_max - 1) / 2 * 2 + 1;
        
        if (x == 0) {
            answer += count;
        } else {
            answer += 2 * count;
        }
    }
    
    // Account for all four quadrants
    answer = answer * 2 - 1;
    
    cout << answer << endl;
    
    return 0;
}