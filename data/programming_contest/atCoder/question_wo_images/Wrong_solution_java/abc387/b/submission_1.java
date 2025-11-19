import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int x = Integer.parseInt(reader.readLine());
        int res = 2025;
        for (int i = 1; i <= 9; i++) {
          int t = x % i;
          if (t == 0) {
            t = x / i;
            if (t > 0 && t <= 9) {
              res -= t;
            }

          }
        }
        System.out.println(res);
    }
}