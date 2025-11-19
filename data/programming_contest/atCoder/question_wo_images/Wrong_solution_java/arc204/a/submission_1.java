import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    private static long action1(long c, int i, Queue<Integer> queue, int[] A) {
        i -= 1;
        queue.add(i);
        c = Math.max(0, c - A[i]);
        return c;
    }

    private static long action2(long c, int i, Queue<Integer> queue, int[] B) {
        int x = queue.poll();
        c += B[x];
        return c;
    }

    private static long check(long c, int l, int r) {
        return Math.min(Math.abs(c - l), Math.abs(c - r));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), L = sc.nextInt(), R = sc.nextInt();
        int A[] = new int[N];
        int B[] = new int[N];
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < N; A[i++] = sc.nextInt())
            ;
        for (int i = 0; i < N; B[i++] = sc.nextInt())
            ;
        int a1 = N, b1 = N, i = 1;
        long count = 1, c = 0;
        for (int m = 0; m < 2 * N; ++m) {
            if (queue.size() == 0) {
                long temp = action1(c, i, queue, A);
                c = temp;
                ++i;
                continue;
            }
            long one = -1, two = -1;
            if (a1 != 0) {
                one = action1(c, i, queue, A);

            }
            if (b1 != 0) {
                two = action2(c, i, queue, B);
            }
            if (a1 == 0) {
                c = two;
                continue;
            }
            if (b1 == 0) {
                c = one;
                continue;
            }
            if (check(one, L, R) > check(two, L, R)) {
                c = two;
                --b1;
            } else if (check(one, L, R) < check(two, L, R)) {
                c = one;
                ++i;
                --a1;
            } else {
                ++count;
                count += (count * (count - 1)) / 2;
                --a1;
                ++i;
            }
            if (c >= L && c <= R) {
                ++count;
                count += (count * (count - 1)) / 2;
            }
            count %= 998244353;
        }
        System.out.println(count - 1);
        sc.close();
    }
}