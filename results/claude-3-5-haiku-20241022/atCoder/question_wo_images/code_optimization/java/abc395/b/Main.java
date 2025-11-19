import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[][] res = new char[n][n];
        
        for (int i = 0; i < n; i++) {
            int row = i;
            int col = n - 1 - i;
            if (row > col) continue;
            
            char ch = (row % 2 == 0) ? '#' : '.';
            
            for (int j = row; j <= col; j++) {
                for (int k = row; k <= col; k++) {
                    res[j][k] = ch;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(res[i][j]);
            }
            System.out.println();
        }
    }
}