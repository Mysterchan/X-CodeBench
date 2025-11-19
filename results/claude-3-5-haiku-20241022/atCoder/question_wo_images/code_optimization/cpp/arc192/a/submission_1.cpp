#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    scanf("%d",&n);
    
    int sum = 0;
    bool has_even_pair = false;
    int last_even = -1, last_odd = -1;
    
    for(int i = 0; i < n; i++)
    {
        int a;
        scanf("%d",&a);
        if(a) {
            sum++;
            if(i % 2 == 0) {
                if(last_even >= 0) has_even_pair = true;
                last_even = i;
            } else {
                if(last_odd >= 0) has_even_pair = true;
                last_odd = i;
            }
        }
    }
    
    if(n % 4 == 0 || ((n % 4 == 1 || n % 4 == 3) && sum > 0) || (n % 4 == 2 && has_even_pair))
        printf("Yes\n");
    else
        printf("No\n");
    
    return 0;
}