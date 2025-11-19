import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        for (int i = 0; i < n; i++) a[i] = sc.nextInt();
        for (int i = 0; i < n; i++) b[i] = sc.nextInt();
        for (int i = 0; i < n; i++) c[i] = sc.nextInt();
        Integer[] op = new Integer[n];
        Integer[] zp = new Integer[n];
        int on = 0, zn = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == 1) op[on++] = i;
            else if (b[i] == 1) zp[zn++] = i;
        }
        Arrays.sort(op, 0, on, (var i, var j) -> { return c[j] - c[i]; });
        Arrays.sort(zp, 0, zn, (var i, var j) -> { return c[i] - c[j]; });
        long ans = 0, pre = 0, suf = 0;
        int j = 0, t = 0, t1 = 0;
        for (int i = on - 1; i >= 0; i--) {
            ans += suf;
            suf += c[op[i]];
            t++;
            if (b[op[i]] == 1) {
                while (j < zn && c[zp[j]] <= c[op[i]]) {
                    pre += c[zp[j]];
                    ans += pre;
                    j++;
                    t1++;
                    t++;
                }
                pre += c[op[i]];
                ans += pre;
                t1++;
                t++;
            }
        }
        while (j < zn) {
            pre += c[zp[j]];
            ans += pre;
            j++;
            t1++;
            t++;
        }

        long cur = ans;
        pre = suf = j = 0;
        long sum1 = 0;
        for (int i = on - 1; i >= 0; i--) {
            if (b[op[i]] == 1) {
                cur -= 1l * i * c[op[i]];
                cur -= suf;
                while (j < zn && c[zp[j]] <= c[op[i]]) {
                    pre += c[zp[j]];
                    j++;
                    t1--;
                }
                cur -= pre;
                cur -= 1l * t1 * c[op[i]];
                t1--;
                t -= 2;
                sum1 += c[op[i]];
                ans = Long.min(ans, cur + 1l * t * sum1);

            } else suf += c[op[i]];
        }
        System.out.println(ans);
    }
}