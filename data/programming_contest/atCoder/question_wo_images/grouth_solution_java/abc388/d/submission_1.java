import java.util.Scanner;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        long[] A = new long[N];
        for (int i = 0; i < N; i++) {
            A[i] = sc.nextLong();
        }

        PriorityQueue<Long> pq = new PriorityQueue<>();

        long[] B = new long[N];

        for (int i = 0; i < N; i++) {

            long offset = i;

            while (!pq.isEmpty() && pq.peek() < offset) {
                pq.poll();
            }

            long giftsReceived = pq.size();

            long stonesAtAdulthood = A[i] + giftsReceived;

            B[i] = stonesAtAdulthood;

            if (stonesAtAdulthood > 0) {

                long runOutOffset = offset + stonesAtAdulthood;
                pq.add(runOutOffset);
            }
        }

        for (int i = 0; i < N; i++) {
            long stones = B[i];
            long askedToGive = N - (i + 1);

            long actualGifts = Math.min(stones, askedToGive);

            B[i] = stones - actualGifts;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(B[i]);
            if (i < N - 1) {
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());

        sc.close();
    }
}