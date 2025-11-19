import java.io.PrintWriter;
import java.util.*;

class Main {
    public static void main(String[] atgs) {
        Scanner sc = new Scanner(System.in);
        PrintWriter pw = new PrintWriter(System.out);

        var T = sc.nextInt();

        for(int t=0; t<T; t++) {
            var N = sc.nextInt();
            var M = sc.nextInt();
            var ans = N * (M / 2) + (M % 2);
            pw.println(ans);
        }

        pw.flush();
        sc.close();
    }
}