import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long L = sc.nextLong();
        long R = sc.nextLong();
        System.out.println(count(R) - count(L - 1));
    }

    static long intPow(long a, int t) {
        long res = 1;
        for (int i = 0; i < t; i++) {
            res *= a;
        }
        return res;
    }

    static long count(long r) {
        List<Integer> digits = new ArrayList<>();
        long temp = r;
        while (temp > 0) {
            digits.add((int)(temp % 10));
            temp /= 10;
        }
        Collections.reverse(digits);
        int n = digits.size();
        long res = 0;

        for (int i = 1; i <= n; i++) {
            if (i == n) {
                res++;
                break;
            }
            res += intPow(digits.get(0), n - 1 - i) * Math.min(digits.get(0), digits.get(i));
            if (digits.get(i) >= digits.get(0)) break;
        }

        for (int i = 0; i < n; i++) {
            int maxDigit = (i == 0) ? digits.get(0) - 1 : 9;
            for (int j = 1; j <= maxDigit; j++) {
                res += intPow(j, n - 1 - i);
            }
        }

        return res;
    }
}