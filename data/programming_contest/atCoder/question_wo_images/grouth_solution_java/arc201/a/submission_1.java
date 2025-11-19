import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for(int i = 0; i < t; i++) {
            solve(sc);
        }
    }

    static void solve(Scanner sc) {
        int n = sc.nextInt();

        long div1Min = 0;
        long div1Max = 0;
        long div2Min = 0;

        long free = 0;

        for(int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            int tmpDiv1 = Math.min(a, b);
            int tmpDiv2 = Math.min(b - tmpDiv1, c);

            div1Max += tmpDiv1;
            div2Min += tmpDiv2;

            int tmpFree = Math.min(tmpDiv1, Math.min(b - tmpDiv2, c - tmpDiv2));

            free += tmpFree;

        }

        if(div1Max < div2Min) {
            System.out.println(div1Max);
        }
        else {
            long result = Math.min((div1Max + div2Min) / 2, div2Min + free);

            System.out.println(result);
        }
    }

}