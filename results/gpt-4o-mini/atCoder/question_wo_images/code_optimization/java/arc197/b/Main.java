import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int t = sc.nextInt();

        while (t-- > 0) {
            solve();
        }

        out.close();
    }

    static void solve() {
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Calculate the total sum and max element in the array
        long totalSum = 0;
        int maxElement = Integer.MIN_VALUE;

        for (int a : arr) {
            totalSum += a;
            if (a > maxElement) {
                maxElement = a;
            }
        }

        // The maximum score of a non-empty subsequence will include all elements 
        // that are greater than the average as long as the average is less than 
        // the maximum element
        double average = (double) totalSum / n;
        int score = 0;

        for (int a : arr) {
            if (a > average) {
                score++;
            }
        }

        out.println(score);
    }
}