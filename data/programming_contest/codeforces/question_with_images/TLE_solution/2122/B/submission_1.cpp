#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<climits>
#include<cmath>

using namespace std;

typedef long long ll;

int main()
{

    int t;
    cin>>t;

    while(t--)
    {
         int n;
        cin>>n;

        ll steps = 0;

        for(int i=0; i<n; i++)
        {
            ll zeros, ones, reqZ, reqO;
            cin>>zeros>>ones>>reqZ>>reqO;

            ll zDiff = zeros - reqZ;
            ll oDiff = ones - reqO;


            if(zDiff > 0)
            {
                steps += zDiff;
            }

            if(oDiff > 0)
            {
                steps += (ones - reqO);
                steps += min(zeros, reqZ);
            }

        }

        cout<<steps<<endl;
    }
    
    return 0;
}