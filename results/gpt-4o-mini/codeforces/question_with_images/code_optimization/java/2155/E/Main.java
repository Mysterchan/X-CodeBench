import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        FastScanner fs = new FastScanner();
        PrintWriter out = new PrintWriter(System.out);
        int t = fs.nextInt();
        while (t-- > 0) {
            int n = fs.nextInt();
            int m = fs.nextInt();
            int k = fs.nextInt();

            Set<Integer> columnsWithTokens = new HashSet<>();
            for (int i = 0; i < k; i++) {
                int r = fs.nextInt();
                int c = fs.nextInt();
                columnsWithTokens.add(c);
            }

            boolean player1 = false;
            if (n == 1) {
                player1 = columnsWithTokens.contains(2);
            } else {
                for (int c = 2; c <= m; c++) {
                    if (columnsWithTokens.contains(c)) {
                        player1 = true;
                        break;
                    }
                }
            }

            out.println(player1 ? "Mimo" : "Yuyu");
        }
        out.flush();
    }

    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tokens = null;
        int index = 0;

        String next() {
            if (tokens == null || index >= tokens.length) {
                try {
                    tokens = br.readLine().split("\\s+");
                    index = 0;
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return tokens[index++];
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}