import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int s = sc.nextInt();
            int k = sc.nextInt();
            int ans = 1;

            if (s % k == 0) {
                ans = k;
            } else if (s >= (long) k * k) {
                ans = Math.max(1, k - 2);
            } else {
                BitSet prev = new BitSet(s + 1);
                for (int i = 0; i <= s; i += k) prev.set(i);

                BitSet curr = new BitSet(s + 1);
                int turns = 0;

                while (!prev.get(s)) {
                    turns++;
                    int step = Math.max(1, k - turns);
                    curr.clear();

                    for (int pos = prev.nextSetBit(0); pos >= 0; pos = prev.nextSetBit(pos + 1)) {
                        for (int j = pos - step; j >= 0; j -= step) {
                            curr.set(j);
                        }
                    }
                    prev.clear();
                    prev.or(curr);
                    if (prev.get(s)) break;

                    turns++;
                    step = Math.max(1, k - turns);
                    curr.clear();

                    for (int pos = prev.nextSetBit(0); pos >= 0; pos = prev.nextSetBit(pos + 1)) {
                        for (int j = pos + step; j <= s; j += step) {
                            curr.set(j);
                        }
                    }
                    prev.clear();
                    prev.or(curr);
                }

                ans = Math.max(1, k - turns);
            }

            System.out.println(ans);
        }
    }
}
