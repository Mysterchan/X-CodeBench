import java.util.*;
import java.util.stream.*;
import java.math.*;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        StringBuilder sb = new StringBuilder(s);
        for(int i = sb.length() - 1; i > 0; i--){
            if(sb.charAt(i - 1) == 'W' && sb.charAt(i) == 'A')sb.replace(i - 1, i + 1 ,"AC");
        }
        System.out.println(sb);
    }

}