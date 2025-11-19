import java.io.*;
import java.util.*;

public class Main {

    static long power(long base, long exp) {
        long result = 1;
        for (int i = 0; i < exp; i++) {
            result *= base;
        }
        return result;
    }

    static long count(long x) {
        if (x < 10) {
            return 0;
        }
        char[] digits = String.valueOf(x).toCharArray();
        int len = digits.length;
        int[] dig = new int[len];
        for (int i = 0; i < len; i++) {
            dig[i] = digits[i] - '0';
        }
        long total = 0;

        for (int i = 1; i <= len; i++) {
            if (i == len) {
                total++;
                break;
            }
            int head = dig[0];
            total += power(head, len - 1 - i) * Math.min(head, dig[i]);
            if (dig[i] >= head) {
                break;
            }
        }

        for (int i = 0; i < len; i++) {
            int upper = (i == 0 ? dig[0] - 1 : 9);
            for (int j = 1; j <= upper; j++) {
                total += power(j, len - 1 - i);
            }
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long L = Long.parseLong(st.nextToken()), R = Long.parseLong(st.nextToken());
        System.out.println(count(R) - count(L - 1));
    }
}