import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String S = sc.next();
        char[] Sargs = S.toCharArray();
        sc.close();

        StringBuilder sb = new StringBuilder();

        for(char score : Sargs){
            if(score == '2'){
                sb.append(score);
            }
            System.out.println(sb.toString());
        }
    }
}