# include <iostream>
# include <vector>

using namespace std ;

int main(){
    int n ,l ; 
    cin >> n >> l;
    int d[n] ;
    vector<vector<int>> p(l,vector<int>(0)) ;
    p[0].push_back(0);
    int s = 0 ;
    for(int i = 0 ; i < n-1 ; i ++){
        int di ;
        cin >> di ;
        s += di ;
        if(s >= l){
            s -= l ;
        }
        p[s].push_back(i+1) ;

    }
    if(l % 3 != 0){
        cout << 0 << endl ;
        return 0 ;
    }
    int resulut = 0 ;
    int length = l/3 ;
    int length2 = l*2/3 ;
    for(int i = 0 ; i < length ; i ++ ){
        for(int elm : p[i]){
            for(int elm2 : p[i + length]){
                for(int elm3 : p[i +length2]){
                    if(elm < elm2 && elm2 < elm3 ){
                        resulut ++ ;
                    }else if(elm2 < elm3 && elm3 < elm ){
                        resulut ++ ;
                    }else if(elm3 < elm && elm < elm2 ){
                        resulut ++ ;
                    }else if(elm > elm2 && elm2 > elm3 ){
                        resulut ++ ;
                    }else if(elm2 > elm3 && elm3 > elm ){
                        resulut ++ ;
                    }else if(elm3 > elm && elm > elm2 ){
                        resulut ++ ;
                    }
                }
            }
        }
    }

    cout << resulut << endl ;
    return 0 ;
}
