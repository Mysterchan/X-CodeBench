import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // Use BufferedReader and BufferedWriter for faster IO
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());

        // pigeonNest[pigeon] = current nest of pigeon p
        int[] pigeonNest = new int[n + 1];
        // nestCount[nest] = number of pigeons in nest
        int[] nestCount = new int[n + 1];

        // Initialize: pigeon i in nest i, so count = 1 for each nest
        for (int i = 1; i <= n; i++) {
            pigeonNest[i] = i;
            nestCount[i] = 1;
        }

        int multiCount = 0; // number of nests with >= 2 pigeons

        for (int i = 0; i < q; i++) {
            String line = br.readLine();
            if (line.charAt(0) == '1') {
                // Query type 1: move pigeon P to nest H
                st = new StringTokenizer(line);
                st.nextToken(); // skip '1'
                int p = Integer.parseInt(st.nextToken());
                int h = Integer.parseInt(st.nextToken());

                int oldNest = pigeonNest[p];

                // Decrement count of old nest
                int oldCount = nestCount[oldNest];
                nestCount[oldNest] = oldCount - 1;
                if (oldCount == 2) {
                    // oldNest was multi, now no longer multi
                    multiCount--;
                }

                // Increment count of new nest
                int newCount = nestCount[h];
                nestCount[h] = newCount + 1;
                if (newCount == 1) {
                    // newNest was single, now multi
                    multiCount++;
                }

                // Update pigeon location
                pigeonNest[p] = h;

            } else {
                // Query type 2: output number of nests with >= 2 pigeons
                bw.write(Integer.toString(multiCount));
                bw.newLine();
            }
        }
        bw.flush();
    }
}