import java.io.*;
import java.util.*;

public class Main {
    static int[] pigeonNest; // pigeonNest[pigeon] = nest
    static int[] nestMap;    // nestMap[nest] = current nest after swaps

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        String[] first = br.readLine().split(" ");
        int N = Integer.parseInt(first[0]);
        int Q = Integer.parseInt(first[1]);

        pigeonNest = new int[N + 1];
        nestMap = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            pigeonNest[i] = i;
            nestMap[i] = i;
        }

        for (int _q = 0; _q < Q; _q++) {
            String line = br.readLine();
            String[] parts = line.split(" ");
            int op = Integer.parseInt(parts[0]);

            if (op == 1) {
                // Move pigeon a to nest b
                int a = Integer.parseInt(parts[1]);
                int b = Integer.parseInt(parts[2]);
                pigeonNest[a] = b;
            } else if (op == 2) {
                // Swap nests a and b
                int a = Integer.parseInt(parts[1]);
                int b = Integer.parseInt(parts[2]);
                int temp = nestMap[a];
                nestMap[a] = nestMap[b];
                nestMap[b] = temp;
            } else {
                // Query pigeon a's current nest
                int a = Integer.parseInt(parts[1]);
                // The actual nest is nestMap[pigeonNest[a]]
                out.println(nestMap[pigeonNest[a]]);
            }
        }

        out.flush();
        out.close();
        br.close();
    }
}