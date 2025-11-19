import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < S.length(); i++) {
            char c = S.charAt(i);
            
            if (c == 'A' && sb.length() > 0 && sb.charAt(sb.length() - 1) == 'W') {
                sb.setCharAt(sb.length() - 1, 'A');
                sb.append('C');
            } else {
                sb.append(c);
            }
        }
        
        System.out.println(sb.toString());
    }
}