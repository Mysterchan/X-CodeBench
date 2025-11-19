import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[] power = new int[n];
        int[] color = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            power[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            color[i] = Integer.parseInt(st.nextToken());
        }

        // Group powers by color using ArrayList[] (1-based indexing)
        ArrayList<Integer>[] groupedByColor = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) {
            groupedByColor[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            groupedByColor[color[i]].add(power[i]);
        }

        long totalCost = 0L;

        // For each color, compute LIS length of the powers in that color
        // Use a primitive int[] and binary search for better performance
        for (int col = 1; col <= n; col++) {
            ArrayList<Integer> seq = groupedByColor[col];
            int size = seq.size();
            if (size == 0) continue;

            int[] lisTails = new int[size];
            int length = 0;

            for (int val : seq) {
                // Binary search for lower bound in lisTails
                int pos = Arrays.binarySearch(lisTails, 0, length, val);
                if (pos < 0) pos = -(pos + 1);
                lisTails[pos] = val;
                if (pos == length) length++;
            }

            totalCost += (long)(size - length) * col;
        }

        System.out.println(totalCost);
    }
}