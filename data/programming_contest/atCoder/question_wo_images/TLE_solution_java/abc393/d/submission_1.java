import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        String s = scanner.next();

        if (N <= 2) {
            System.out.println(0);
            return;
        }

        List<Integer> ones = new ArrayList<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                ones.add(i);
            }
        }

        if (ones.size() < 2) {
            System.out.println(0);
            return;
        }

        int ans = Integer.MAX_VALUE;

        for (int i = 0; i < ones.size(); i++) {
            ans = Math.min(ans, solve(ones, i));
        }

        System.out.println(ans);
    }

    private static int solve(List<Integer> ones, int mid) {
        int mVal = ones.get(mid);

        int sum = 0;

        for (int i = mid - 1; i >= 0; i--) {
            sum += (mVal - ones.get(i) - 1 - (mid - i - 1));
        }

        for (int i = mid + 1; i < ones.size(); i++) {
            sum += (ones.get(i) - mVal - 1 - (i - mid - 1));
        }

        return sum;
    }
}