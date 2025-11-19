import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(reader.readLine());
        String[] input = reader.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        long sum = 0, maxSum = Long.MIN_VALUE;

        for (int value : arr) {
            sum += value;
            if (sum < 0) {
                sum = 0; // Reset sum if it goes negative
            }
            maxSum = Math.max(maxSum, sum);
        }

        System.out.println(maxSum);
    }
}