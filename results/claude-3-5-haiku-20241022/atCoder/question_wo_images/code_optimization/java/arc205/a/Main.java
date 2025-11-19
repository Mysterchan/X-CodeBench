import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int q = sc.nextInt();

        char[][] matrix = new char[n][n];

        for(int i = 0; i < n; i++) {
            matrix[i] = sc.next().toCharArray();
        }

        for(int i = 0; i < q; i++) {
            int u = sc.nextInt() - 1;
            int d = sc.nextInt() - 1;
            int l = sc.nextInt() - 1;
            int r = sc.nextInt() - 1;
            
            int count = 0;
            for(int row = u; row < d; row++) {
                for(int col = l; col < r; col++) {
                    if(matrix[row][col] == '.' && 
                       matrix[row][col + 1] == '.' && 
                       matrix[row + 1][col] == '.' && 
                       matrix[row + 1][col + 1] == '.') {
                        count++;
                    }
                }
            }
            
            System.out.println(count);
        }
    }
}