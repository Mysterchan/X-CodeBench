import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }

        for (int i = 0; i < n; i++) {
            b[i] = scanner.nextInt();
        }

        for (int i = 0; i < n; i++) {
            c[i] = scanner.nextInt();
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> y - x);
        long cost = 0;
        long sum = 0;

        for (int i = 0; i < n; i++) {
            if (a[i] != b[i]) {
                pq.add(c[i]);
            }
            sum += a[i] * c[i];
        }

        while (!pq.isEmpty()) {
            int max = pq.poll();
            sum -= max;
            cost += sum;
            a[binarySearch(a, b)] ^= 1;
            sum += max;
        }

        System.out.println(cost);
    }

    public static int binarySearch(int[] a, int[] b) {
        int left = 0;
        int right = a.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (a[mid] != b[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}