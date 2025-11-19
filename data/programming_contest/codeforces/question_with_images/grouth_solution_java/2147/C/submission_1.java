import java.util.*;
import java.util.regex.*;

public final class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        Pattern pattern = Pattern.compile("11(0101)*011");

        while (T-- > 0) {
            int n = sc.nextInt();
            String s = "1" + sc.next() + "1"; 

            Matcher matcher = pattern.matcher(s);
            if (matcher.find()) {
                System.out.println("NO");
            } else {
                System.out.println("YES");
            }
        }

        sc.close();
    }
}
