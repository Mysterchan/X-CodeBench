import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        if (t >= 1 && t <= 100)
        {
            for(int i = 0; i < 2; i++) {
                int teams = sc.nextInt();
                System.out.println(2*teams-2);
            }
        }
        }
}
