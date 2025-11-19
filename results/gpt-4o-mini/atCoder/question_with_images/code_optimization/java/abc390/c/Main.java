import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();
        sc.nextLine(); // Consume the newline character

        int wMin = W, wMax = -1, hMin = H, hMax = -1;
        boolean hasBlack = false;

        // Read the grid and determine the bounds of the black cells
        for (int i = 0; i < H; i++) {
            String row = sc.nextLine();
            for (int j = 0; j < W; j++) {
                if (row.charAt(j) == '#') {
                    hasBlack = true;
                    wMin = Math.min(wMin, j);
                    wMax = Math.max(wMax, j);
                    hMin = Math.min(hMin, i);
                    hMax = Math.max(hMax, i);
                }
            }
        }

        // If there are no black cells, it's impossible
        if (!hasBlack) {
            System.out.println("No");
            return;
        }

        // Check if all cells in the bounding rectangle are valid
        for (int i = hMin; i <= hMax; i++) {
            for (int j = 0; j < W; j++) {
                char cell = sc.nextLine().charAt(j);
                if (i >= hMin && i <= hMax && j >= wMin && j <= wMax) {
                    if (cell == '.') {
                        System.out.println("No");
                        return;
                    }
                } else {
                    if (cell == '#') {
                        System.out.println("No");
                        return;
                    }
                }
            }
        }

        System.out.println("Yes");
    }
}