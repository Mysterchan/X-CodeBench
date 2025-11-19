#include<iostream>;
using namespace std;

int main()
{
    string D ;
    cin >> D ;

    if ( D == "N" )
    {
    cout << "S" << endl;
    }


     else if ( D == "S")
    {
     cout << "N" ;
    }


     else if ( D == "E")
    {
     cout << "W" ;
    }


     else if (D == "W")
    {
     cout << "E" ;
    }


     else if (D == "NE")
    {
     cout << "SW" ;
    }


     else if (D == "NW")
    {
     cout << "SE" ;
    }

     else if (D == "SE")
    {
     cout << "NW" ;
    }

     else if (D == "SW")
    {
     cout << "NE" ;
    }


    return 0;
}
