import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder(sc.next());
        int i = 0;
        while (i < sb.length() - 1) {
            if (sb.charAt(i) == 'W' && sb.charAt(i + 1) == 'A') {
                sb.replace(i, i + 2, "AC");
                i = Math.max(0, i - 1); // Move back one index to check for new "WA" that might have formed
            } else {
                i++;
            }
        }
        System.out.println(sb);
    }
}