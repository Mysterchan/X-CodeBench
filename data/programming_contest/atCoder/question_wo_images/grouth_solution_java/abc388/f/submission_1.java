import java.util.Scanner;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long N = sc.nextLong();
        int M = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();

        long[] L = new long[M];
        long[] R = new long[M];
        for (int i = 0; i < M; i++) {
            L[i] = sc.nextLong();
            R[i] = sc.nextLong();
        }
        sc.close();

        long check_mask = 0;
        for (int i = A; i <= B; i++) {
            check_mask |= (1L << (i - 1));
        }

        long mask_limit = (1L << B) - 1;

        long mask = 1L;

        HashMap<Long, Long> seen = new HashMap<>();

        long x = 2;
        int bad_ptr = 0;

        while (x <= N) {
            long next_event_start = N + 1;
            if (bad_ptr < M) {
                next_event_start = L[bad_ptr];
            }

            if (x >= next_event_start) {

                if (x > R[bad_ptr]) {
                    bad_ptr++;
                    continue;
                }

                long end_bad = R[bad_ptr];
                long steps_to_skip = Math.min(N, end_bad) - x + 1;

                if (steps_to_skip > 0) {

                    mask = (mask << steps_to_skip);
                    mask &= mask_limit;
                    x += steps_to_skip;
                }
                bad_ptr++;

            } else {

                long end_good = Math.min(N, next_event_start - 1);

                seen.clear();

                while (x <= end_good) {
                    if (seen.containsKey(mask)) {

                        long prev_x = seen.get(mask);
                        long cycle_len = x - prev_x;
                        long steps_to_go = end_good - x;

                        if (steps_to_go >= cycle_len) {
                            long num_cycles = steps_to_go / cycle_len;
                            x += num_cycles * cycle_len;
                        }
                        seen.clear();
                    }
                    seen.put(mask, x);

                    boolean canReach = (mask & check_mask) != 0;

                    mask = (mask << 1) | (canReach ? 1L : 0L);
                    mask &= mask_limit;
                    x++;
                }
            }
        }

        if ((mask & 1L) != 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}