import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long Rt = sc.nextLong();
        long Ct = sc.nextLong();
        long Ra = sc.nextLong();
        long Ca = sc.nextLong();
        long n = sc.nextLong();
        int m = sc.nextInt();
        int L = sc.nextInt();
        String sT ="";
        String sC= "";
        String sign;
        long times ;
        for (int i = 0; i < m; i++) {
            sign = sc.next();
            times = sc.nextLong();
            for (long j = 0; j < times; j++) {
                sT += sign;
            }
        }
        for (int i = 0; i < L; i++) {
            sign = sc.next();
            times = sc.nextInt();
            for (long j = 0; j < times; j++) {
                sC += sign;
            }
        }
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (sT.charAt(i) == 'U') {
               Rt--;
            }
            if (sT.charAt(i) == 'D') {
               Rt++;
            }
             if (sT.charAt(i) == 'L') {
               Ct--;
            }
            if (sT.charAt(i) == 'R') {
              Ct++;
            }

            if (sC.charAt(i) == 'U') {
              Ra--;
            }
            if (sC.charAt(i) == 'D') {
               Ra++;
            }
             if (sC.charAt(i) == 'L') {
               Ca--;
            }
            if (sC.charAt(i) == 'R') {
               Ca++;
            }
            if (Rt == Ra && Ct == Ca) {
                count++;
            }

        }
        System.out.println(count);

    }

}