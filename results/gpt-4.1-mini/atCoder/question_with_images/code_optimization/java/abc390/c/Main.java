import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        String[] S = new String[H];
        for (int i = 0; i < H; i++) {
            S[i] = sc.next();
        }

        int hMin = H, hMax = -1, wMin = W, wMax = -1;

        // Find bounding rectangle of black cells
        for (int i = 0; i < H; i++) {
            String row = S[i];
            for (int j = 0; j < W; j++) {
                if (row.charAt(j) == '#') {
                    if (i < hMin) hMin = i;
                    if (i > hMax) hMax = i;
                    if (j < wMin) wMin = j;
                    if (j > wMax) wMax = j;
                }
            }
        }

        // If no black cells, check if any '?' exists
        if (hMax == -1) {
            for (int i = 0; i < H; i++) {
                if (S[i].indexOf('?') >= 0) {
                    System.out.println("Yes");
                    return;
                }
            }
            System.out.println("No");
            return;
        }

        // Check cells inside bounding rectangle
        for (int i = hMin; i <= hMax; i++) {
            String row = S[i];
            for (int j = wMin; j <= wMax; j++) {
                char c = row.charAt(j);
                if (c == '.') {
                    // White cell inside black rectangle -> impossible
                    System.out.println("No");
                    return;
                }
            }
        }

        // Check cells outside bounding rectangle
        for (int i = 0; i < H; i++) {
            String row = S[i];
            for (int j = 0; j < W; j++) {
                if (i >= hMin && i <= hMax && j >= wMin && j <= wMax) continue;
                char c = row.charAt(j);
                if (c == '#') {
                    // Black cell outside bounding rectangle -> impossible
                    System.out.println("No");
                    return;
                }
            }
        }

        System.out.println("Yes");
    }
}