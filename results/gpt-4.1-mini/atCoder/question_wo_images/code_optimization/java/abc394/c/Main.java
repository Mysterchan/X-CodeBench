import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] s = sc.next().toCharArray();
        int n = s.length;
        // We'll process the string from left to right,
        // replacing each occurrence of "WA" with "AC" immediately,
        // and then continue scanning from the previous position to catch overlapping occurrences.

        for (int i = 0; i < n - 1; ) {
            if (s[i] == 'W' && s[i + 1] == 'A') {
                s[i] = 'A';
                s[i + 1] = 'C';
                // Move back one position to catch overlapping "WA" that may have formed
                if (i > 0) i--;
                else i++;
            } else {
                i++;
            }
        }
        System.out.println(new String(s));
    }
}