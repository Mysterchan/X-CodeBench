import java.io.*;
import java.util.*;

public class Main {

    static Scanner sc;
    static PrintWriter out;

    public static void main(String[] args) {
        sc = new Scanner(System.in);
        out = new PrintWriter(System.out);
        new Main().solve();
        out.flush();
    }

    public void solve() {
        long r = sc.nextInt() * 2;
        long res = 0;
        long x = r + 1;
        for(int y = 1; y < r; y+=2){
            while(x>0 && x*x + y*y > r*r) {
                x-=2;
            }
            if(x<0) break;
            if(y == 1) {
                res += x;
            } else {
                res += x * 2;
            }
        }
        out.println(res);

    }

}