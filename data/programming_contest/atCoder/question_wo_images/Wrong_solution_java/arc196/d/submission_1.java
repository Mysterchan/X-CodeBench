import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int M = Integer.parseInt(line[1]);
        int Q = Integer.parseInt(line[2]);

        int[][] people = new int[M][2];
        for (int i = 0; i < M; i++) {
            line = br.readLine().split(" ");
            people[i][0] = Integer.parseInt(line[0]);
            people[i][1] = Integer.parseInt(line[1]);
        }

        for (int i = 0; i < Q; i++) {
            line = br.readLine().split(" ");
            int L = Integer.parseInt(line[0]) - 1;
            int R = Integer.parseInt(line[1]) - 1;
            boolean satisfied = true;

            System.out.println(satisfied ? "Yes" : "No");
        }
    }
}