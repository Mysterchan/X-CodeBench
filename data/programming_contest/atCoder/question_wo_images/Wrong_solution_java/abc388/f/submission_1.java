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

        long mask = 1L;
        long mask_limit = (1L << B) - 1;

        HashMap<Long, Long> seen = new HashMap<>();

        long x = 1;
        int bad_ptr = 0;

        while (x < N) {
            long next_event_start = N + 1;
            if (bad_ptr < M) {
                next_event_start = L[bad_ptr];
            }

            long end_good = Math.min(N, next_event_start - 1);

            seen.clear();
            while (x <= end_good) {
                if (seen.containsKey(mask)) {

                    long prev_x = seen.get(mask);
                    long cycle_len = x - prev_x;
                    long steps_to_go = end_good - x;

                    if (steps_to_go > 0) {
                        long num_cycles = steps_to_go / cycle_len;
                        x += num_cycles * cycle_len;
                    }
                    seen.clear();
                }
                seen.put(mask, x);

                if (x == N) break;

                boolean canReach = (mask & check_mask) != 0;

                mask = (mask << 1) | (canReach ? 1L : 0L);
                mask &= mask_limit;
                x++;
            }

            if (x > N) break;

            if (bad_ptr < M && x == L[bad_ptr]) {
                long num_bad_squares = R[bad_ptr] - L[bad_ptr] + 1;

                long actual_bad_steps = Math.min(N, R[bad_ptr]) - x + 1;

                if (actual_bad_steps > 0) {

                    mask = (mask << actual_bad_steps);
                    mask &= mask_limit;
                    x += actual_bad_steps;
                }
                bad_ptr++;
            }
        }

        if ((mask & 1L) != 0) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}