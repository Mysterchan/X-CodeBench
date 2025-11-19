import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        int count=0;
        int b=0;
if (S.length()%2==0){
    b=S.length()/2-2;
}
 else {b=S.length()/2-1;}

            for (int d = 1; d <= (S.length()+b)/3; d++) {

                for (int i = 1+d-1; i <=S.length()-1-d ; i++) {
                    if (S.charAt(i-d)=='A'&&S.charAt(i)=='B'&&S.charAt(i+d)=='C'){

                        count++;
                    }

                }

            }

        System.out.println(count);

    }
}