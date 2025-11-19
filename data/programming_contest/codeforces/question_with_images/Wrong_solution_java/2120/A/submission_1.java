import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        for(int i=1; i<=n; i++){
            int l1 = scanner.nextInt();
            int b1 = scanner.nextInt();
            int l2 = scanner.nextInt();
            int b2 = scanner.nextInt();
            int l3 = scanner.nextInt();
            int b3 = scanner.nextInt();
            double area = (l1*b1) + (l2*b2) + (l3*b3);
            double x = Math.sqrt(area);
            double y = Math.floor(x);
            if (x==y){
                System.out.println("YES");
            }
            else{
                System.out.println("NO");
            }
        }

        scanner.close();
    }
}
