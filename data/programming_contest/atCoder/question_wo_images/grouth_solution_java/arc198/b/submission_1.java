import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        for(int t0 = input.nextInt(); t0>0; t0--){
            int X = input.nextInt();
            int Y = input.nextInt();
            int Z = input.nextInt();
            String flag = "Yes";
            if(Z>X || Y>X*2){flag = "No";}
            if(Z == 0 && Y%2 == 1){flag = "No";}
            System.out.println(flag);
        }
    }
}