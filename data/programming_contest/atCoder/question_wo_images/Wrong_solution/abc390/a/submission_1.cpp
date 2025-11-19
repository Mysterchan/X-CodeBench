#include <iostream>
#include <iomanip>
#include <string>
#include <thread>
#include <chrono>
#include <random>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>

int main()
{
    std::vector<int> v(5);
    for (auto& elem : v)
    {
        std::cin >> elem;
    }
    std::vector<int> c = {1,2,3,4,5};
    int s;
    
    int count = 0;
    for(int i = 0; i < 5; ++i)
    {
        if(v[i] != c[i])
        {
            ++count;
            std::cin >> s;
        }
    }
    if(v != c && count < 2)
    {
        std::cout << "Yes\n";
    }
    else if(s/10 - 1 == s%10 || s/10 + 1 == s%10)
    {
        std::cout << "Yes\n";
    }
    else
    {
        std::cout << "No\n";
    }
}

